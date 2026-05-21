/* Copyright (c) 2026 o6 Automation GmbH
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published
 * by the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program. If not, see <https://www.gnu.org/licenses/>.
 */

#include "module.h"
#include "object.h"
#include <open62541/plugin/eventloop.h>
#include <open62541/plugin/log.h>
#include <open62541/types.h>

static void
AsyncIOLoop_lock(AsyncIOLoop *public_el) {
    Py_BEGIN_ALLOW_THREADS
    UA_LOCK(&((AsyncIOLoop*)public_el)->elMutex);
    Py_END_ALLOW_THREADS
}
static void
AsyncIOLoop_unlock(AsyncIOLoop *public_el) {
    UA_UNLOCK(&((AsyncIOLoop*)public_el)->elMutex);
}

/*********/
/* Clock */
/*********/

static UA_DateTime
AsyncIOLoop_now(AsyncIOLoop *el) {
    return UA_DateTime_now();
}

static UA_Int64
AsyncIOLoop_localTimeUtcOffset(AsyncIOLoop *el) {
    return 0;
}

static UA_DateTime
AsyncIOLoop_nowMonotonic(AsyncIOLoop *el) {
    UA_assert(el->pyLoop);

    PyObject *result = PyObject_CallMethod(el->pyLoop, "time", NULL);
    if(!result) {
        PyErr_Print();
        UA_LOG_ERROR(el->cLoop.logger, UA_LOGCATEGORY_EVENTLOOP,
                     "Accessing the monotonic clock failed");
        return -1.0;
    }

    double time_value = PyFloat_AsDouble(result);
    Py_DECREF(result);

    if(PyErr_Occurred()) {
        PyErr_Print();
        UA_LOG_ERROR(el->cLoop.logger, UA_LOGCATEGORY_EVENTLOOP,
                     "Converting the monotonic datetime failed");
        return -1.0;
    }

    return (UA_DateTime)(time_value * UA_DATETIME_SEC);
}

/*********/
/* Timer */
/*********/

struct PyUATimer {
    PyObject_HEAD
    LIST_ENTRY(PyUATimer) pointers;
    UA_TimerPolicy timerPolicy;
    UA_DateTime nextTime;
    UA_DateTime interval;
    UA_Callback cb;
    void *application;
    void *data;
    UA_UInt64 id;
    AsyncIOLoop *el;
    PyObject *timerHandle; // Returned by loop.call_at(), required to cancel
};

static PyObject * executePyUATimer(PyObject *self, PyObject *args, PyObject *kwargs);
static void deleteTimer(PyObject *self);

PyTypeObject PyUATimerType = {
    .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "o6.Timer",
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_basicsize = sizeof(PyUATimer),
    .tp_call = executePyUATimer,
    .tp_new = PyType_GenericNew,
    .tp_finalize = deleteTimer
};

// Taken from timer.c.
// Short enough not to make license issues
static UA_DateTime
calculateNextTime(UA_DateTime currentTime, UA_DateTime baseTime,
                  UA_DateTime interval) {
    UA_DateTime diffCurrentTimeBaseTime = currentTime - baseTime;
    UA_DateTime cycleDelay = diffCurrentTimeBaseTime % interval;
    if(UA_UNLIKELY(cycleDelay < 0))
        cycleDelay += interval;
    return currentTime + interval - cycleDelay;
}

static void insertTimer(PyUATimer *t) {
    AsyncIOLoop *el = t->el;
    /* Convert from our monotonic ticks (loop.time() * UA_DATETIME_SEC)
     * back to asyncio loop time (seconds). */
    double callTime = ((double)t->nextTime) / UA_DATETIME_SEC;
    t->timerHandle = PyObject_CallMethod(el->pyLoop, "call_at", "dO", callTime, t);
    if(t->timerHandle) {
        LIST_INSERT_HEAD(&el->timers, t, pointers);
    } else {
        PyErr_Clear();
        UA_LOG_ERROR(el->cLoop.logger, UA_LOGCATEGORY_EVENTLOOP,
                     "Could not re-register cyclic timer");
    }
}

static void deleteTimer(PyObject *self) {
    PyUATimer *t = (PyUATimer*)self;
    if(t->timerHandle) {
        Py_DECREF(t->timerHandle);
        t->timerHandle = NULL;
    }
    /* Always remove from whichever list (timers / delayedTimers) the timer
     * is in.  le_prev is non-NULL when the timer is linked.  We null it
     * after removal so that a second deleteTimer / LIST_REMOVE is a no-op. */
    if(t->el && t->pointers.le_prev != NULL) {
        LIST_REMOVE(t, pointers);
        t->pointers.le_prev = NULL;
    }
}

static PyObject *
executePyUATimer(PyObject *self, PyObject *args, PyObject *kwargs) {
    PyUATimer *t = (PyUATimer*)self;
    /* Execute the callback */
    if(t->cb)
        t->cb(t->application, t->data);

    /* Remove the timerHandle - too late to cancel the timer.
     * Use Py_XDECREF in case timerHandle was already cleared by AsyncIOLoop_free. */
    Py_XDECREF(t->timerHandle);
    t->timerHandle = NULL;

    /* Do not reinsert if marked for deletion or a "once" policy.
     * Remove from el->timers / el->delayedTimers (reuse pointers field). */
    if(!t->cb || t->timerPolicy == UA_TIMERPOLICY_ONCE) {
        if(t->el && t->pointers.le_prev != NULL) {
            LIST_REMOVE(t, pointers);
            t->pointers.le_prev = NULL;
        }
        return Py_None;
    }

    /* Set the time for the next regular execution */
    t->nextTime += t->interval;

    /* Handle the case where the execution "window" was missed. E.g. due to
     * congestion of the application or if the clock was shifted. */
    UA_DateTime nowM = AsyncIOLoop_nowMonotonic(t->el);
    if(t->nextTime < nowM) {
        t->nextTime = (t->timerPolicy == UA_TIMERPOLICY_CURRENTTIME) ?
            nowM + t->interval : calculateNextTime(nowM, t->nextTime, t->interval);
    }

    /* Remove from el->timers before re-inserting; insertTimer calls
     * LIST_INSERT_HEAD which would corrupt the list on a double-insert. */
    if(t->pointers.le_prev != NULL) {
        LIST_REMOVE(t, pointers);
        t->pointers.le_prev = NULL;
    }

    /* Insert back into the loop */
    insertTimer(t);
    return Py_None;
}

static UA_DateTime AsyncIOLoop_nextTimer(UA_EventLoop *public_el) {
    /* Not meaningful here, since asyncio handles the timer scheduling. */
    return UA_INT64_MIN;
}

static UA_StatusCode
AsyncIOLoop_addTimer(UA_EventLoop *public_el, UA_Callback cb,
                     void *application, void *data, UA_Double interval_ms,
                     UA_DateTime *baseTime, UA_TimerPolicy timerPolicy,
                     UA_UInt64 *callbackId) {
    AsyncIOLoop *el = (AsyncIOLoop*)public_el;
    UA_DateTime nowM = AsyncIOLoop_nowMonotonic(el);

    // Compute interval
    UA_DateTime interval = (UA_DateTime)(interval_ms * UA_DATETIME_MSEC);
    if(interval <= 0) {
        if(timerPolicy != UA_TIMERPOLICY_ONCE)
            return UA_STATUSCODE_BADINTERNALERROR;
        if(baseTime) {
            interval = *baseTime - nowM;
            baseTime = NULL;
        }
    }

    // Compute the first time for execution
    UA_DateTime nextTime = (baseTime == NULL) ?
        nowM + interval : calculateNextTime(nowM, *baseTime, interval);

    // Create new timer
    PyUATimer *t = (PyUATimer*)PyUATimerType.tp_new(&PyUATimerType, NULL, NULL);
    if(!t)
        return UA_STATUSCODE_BADOUTOFMEMORY;

    // Set the members
    t->cb = cb;
    t->application = application;
    t->data = data;
    t->interval = interval;
    t->nextTime = nextTime;
    t->timerPolicy = timerPolicy;
    t->el = el;
    t->id = el->timerIndex++;

    // Insert
    insertTimer(t);

    // Report the timer id back to the caller
    if(callbackId)
        *callbackId = t->id;

    if(!t->timerHandle) {
        // insertTimer failed (call_at returned NULL) — timer was not
        // registered.  Py_DECREF frees the timer.
        Py_DECREF(t);
        return UA_STATUSCODE_BADINTERNALERROR;
    }

    // The only ref is kept in the EventLoop now
    Py_DECREF(t);
    return UA_STATUSCODE_GOOD;
}

static UA_StatusCode
AsyncIOLoop_modifyTimer(UA_EventLoop *public_el, UA_UInt64 callbackId,
                        UA_Double interval_ms, UA_DateTime *baseTime,
                        UA_TimerPolicy timerPolicy) {
    AsyncIOLoop *el = (AsyncIOLoop*)public_el;

    // Get the current timer
    PyUATimer *t;
    int count = 0;
    LIST_FOREACH(t, &el->timers, pointers) {
        count++;
        if(t->id == callbackId)
            break;
    }
    if(!t)
        return UA_STATUSCODE_BADNOTFOUND;


    // Create a new timer to replace
    PyUATimer *t2 = (PyUATimer*)PyUATimerType.tp_new(&PyUATimerType, NULL, NULL);
    if(!t2)
        return UA_STATUSCODE_BADOUTOFMEMORY;

    // Modify
    UA_DateTime nowM = AsyncIOLoop_nowMonotonic(t->el);
    UA_DateTime interval = (UA_DateTime)(interval_ms * UA_DATETIME_MSEC);
    if(interval <= 0) {
        if(timerPolicy != UA_TIMERPOLICY_ONCE)
            return UA_STATUSCODE_BADINTERNALERROR;
        /* Ensure that (nowM + interval) == *baseTime for setting nextTime */
        if(baseTime) {
            interval = *baseTime - nowM;
            baseTime = NULL;
        }
    }

    /* The nextTime must only be modified after ZIP_REMOVE. The logic is
     * identical to the creation of a new timer. */
    UA_DateTime nextTime = (baseTime == NULL) ?
        nowM + interval : calculateNextTime(nowM, *baseTime, interval);

    t2->cb = t->cb;
    t2->application = t->application;
    t2->data = t->data;
    t2->interval = interval;
    t2->nextTime = nextTime;
    t2->timerPolicy = timerPolicy;
    t2->el = t->el;
    t2->id = t->id;
    insertTimer(t2);
    if(!t2->timerHandle) {
        Py_DECREF(t2);
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    Py_DECREF(t2);

    // Success -- cancel the old Timer
    LIST_REMOVE(t, pointers);
    t->pointers.le_prev = NULL;
    /* Save handle to local and detach from t BEFORE cancel.
     * cancel() clears handle._callback which DECREFs t.
     * If t's refcnt is 1 (only from handle._callback), this frees t.
     * Accessing t->timerHandle after that would be use-after-free. */
    {
        PyObject *handle = t->timerHandle;
        t->timerHandle = NULL;
        PyObject *cr = PyObject_CallMethod(handle, "cancel", NULL);
        if(!cr) PyErr_Clear();
        Py_XDECREF(cr);
        Py_DECREF(handle);
    }
    return UA_STATUSCODE_GOOD;
}

static void
AsyncIOLoop_removeTimer(UA_EventLoop *public_el,
                        UA_UInt64 callbackId) {
    AsyncIOLoop *el = (AsyncIOLoop*)public_el;
    PyUATimer *t, *t_tmp;
    LIST_FOREACH_SAFE(t, &el->timers, pointers, t_tmp) {
        if(t->id == callbackId) {
            t->cb = NULL;
            LIST_REMOVE(t, pointers);
            t->pointers.le_prev = NULL;
            /* Save handle to local and detach from t BEFORE cancel.
             * cancel() clears handle._callback which DECREFs t.
             * If t's only ref was from handle._callback, this frees t. */
            if(t->timerHandle) {
                PyObject *handle = t->timerHandle;
                t->timerHandle = NULL;
                PyObject *cr = PyObject_CallMethod(handle, "cancel", NULL);
                if(!cr) PyErr_Clear();
                Py_XDECREF(cr);
                Py_DECREF(handle);
            }
            break;
        }
    }
}

/********************/
/* Delayed Callback */
/********************/

static void
processDelayed(AsyncIOLoop *el, void *_) {
    UA_DelayedCallback *list = el->delayed;
    el->delayed = NULL;
    UA_DelayedCallback *next;
    for(UA_DelayedCallback *cur = list; cur; cur = next) {
        next = cur->next; // Allow dc to free itself
        cur->callback(cur->application, cur->context);
    }
}

static void
AsyncIOLoop_addDelayedCallback(UA_EventLoop *public_el, UA_DelayedCallback *dc) {
    // Add to the linked list
    AsyncIOLoop *el = (AsyncIOLoop*)public_el;
    dc->next = el->delayed;
    el->delayed = dc;

    // Schedule the task for executing the delayed callbacks
    PyUATimer *t = (PyUATimer*)PyUATimerType.tp_new(&PyUATimerType, NULL, NULL);
    if(!t)
        return;
    t->cb = (UA_Callback)processDelayed;
    t->application = el;
    t->data = NULL;
    t->timerPolicy = UA_TIMERPOLICY_ONCE;
    t->el = el;

    // Store the handle so we can cancel it in AsyncIOLoop_free if needed.
    // This also prevents Py_DECREF(NULL) in executePyUATimer.
    t->timerHandle = PyObject_CallMethod(el->pyLoop, "call_soon_threadsafe", "O", t);
    if(!t->timerHandle)
        PyErr_Clear();

    // Track in delayedTimers so AsyncIOLoop_free can cancel before freeing el.
    // Must happen BEFORE Py_DECREF: if call_soon_threadsafe failed,
    // timerHandle is NULL and Py_DECREF frees t — reading t afterwards
    // is use-after-free (crashes under debug allocators that fill 0xDD).
    if(t->timerHandle)
        LIST_INSERT_HEAD(&el->delayedTimers, t, pointers);

    Py_DECREF(t); // asyncio Handle holds a ref to t via the callable
}

static void
AsyncIOLoop_removeDelayedCallback(UA_EventLoop *public_el, UA_DelayedCallback *dc) {
    AsyncIOLoop *el = (AsyncIOLoop*)public_el;
    for(UA_DelayedCallback **cur = &el->delayed; *cur; cur = &(*cur)->next) {
        if(*cur == dc) {
            *cur = (*cur)->next;
            break;
        }
    }
}

/*****************/
/* Event Sources */
/*****************/

static UA_StatusCode
AsyncIOLoop_registerEventSource(AsyncIOLoop *el,
                                UA_EventSource *es) {
    /* Already registered? */
    if(es->state != UA_EVENTSOURCESTATE_FRESH &&
       es->state != UA_EVENTSOURCESTATE_STOPPED) {
        UA_LOG_ERROR(el->cLoop.logger, UA_LOGCATEGORY_NETWORK,
                     "Cannot register the EventSource \"%.*s\": "
                     "already registered",
                     (int)es->name.length, (char*)es->name.data);
        return UA_STATUSCODE_BADINTERNALERROR;
    }

    /* Add to linked list */
    es->next = el->cLoop.eventSources;
    el->cLoop.eventSources = es;

    es->eventLoop = &el->cLoop;
    es->state = UA_EVENTSOURCESTATE_STOPPED;

    /* Start if the entire EventLoop is started */
    UA_StatusCode res = UA_STATUSCODE_GOOD;
    if(el->cLoop.state == UA_EVENTLOOPSTATE_STARTED)
        res = es->start(es);
    return res;
}

static UA_StatusCode
AsyncIOLoop_deregisterEventSource(AsyncIOLoop *el,
                                  UA_EventSource *es) {
  if(es->state != UA_EVENTSOURCESTATE_FRESH &&
     es->state != UA_EVENTSOURCESTATE_STOPPED) {
        UA_LOG_WARNING(el->cLoop.logger, UA_LOGCATEGORY_EVENTLOOP,
                       "Cannot deregister the EventSource %.*s: "
                       "Has to be stopped first",
                       (int)es->name.length, es->name.data);
        return UA_STATUSCODE_BADINTERNALERROR;
    }

    /* Remove from the linked list */
    UA_EventSource **s = &el->cLoop.eventSources;
    while(*s) {
        if(*s == es) {
            *s = es->next;
            break;
        }
        s = &(*s)->next;
    }

    /* Set the state to non-registered */
    es->state = UA_EVENTSOURCESTATE_FRESH;
    return UA_STATUSCODE_GOOD;
}

/***********************/
/* EventLoop Lifecycle */
/***********************/

static UA_StatusCode
AsyncIOLoop_start(AsyncIOLoop *el) {
    UA_LOCK(&el->elMutex);

    if(el->cLoop.state != UA_EVENTLOOPSTATE_FRESH &&
       el->cLoop.state != UA_EVENTLOOPSTATE_STOPPED) {
        UA_UNLOCK(&el->elMutex);
        return UA_STATUSCODE_BADINTERNALERROR;
    }

    UA_LOG_DEBUG(el->cLoop.logger, UA_LOGCATEGORY_EVENTLOOP,
                 "Starting the EventLoop");

    /* Start the EventSources */
    UA_StatusCode res = UA_STATUSCODE_GOOD;
    UA_EventSource *es = el->cLoop.eventSources;
    while(es) {
        res |= es->start(es);
        es = es->next;
    }

    /* Dirty-write the state that is const "from the outside" */
    *(UA_EventLoopState*)(uintptr_t)&el->cLoop.state = UA_EVENTLOOPSTATE_STARTED;

    UA_UNLOCK(&el->elMutex);
    return res;
}

static void
checkClosed(AsyncIOLoop *el) {
    UA_LOCK_ASSERT(&el->elMutex);

    UA_EventSource *es = el->cLoop.eventSources;
    while(es) {
        if(es->state != UA_EVENTSOURCESTATE_STOPPED)
            return;
        es = es->next;
    }

    /* Dirty-write the state that is const "from the outside" */
    *(UA_EventLoopState*)(uintptr_t)&el->cLoop.state = UA_EVENTLOOPSTATE_STOPPED;

    UA_LOG_DEBUG(el->cLoop.logger, UA_LOGCATEGORY_EVENTLOOP, "The EventLoop has stopped");
}

static void
AsyncIOLoop_stop(AsyncIOLoop *el) {
    UA_LOCK(&el->elMutex);

    if(el->cLoop.state != UA_EVENTLOOPSTATE_STARTED) {
        UA_LOG_WARNING(el->cLoop.logger, UA_LOGCATEGORY_EVENTLOOP,
                       "The EventLoop is not running, cannot be stopped");
        UA_UNLOCK(&el->elMutex);
        return;
    }

    UA_LOG_DEBUG(el->cLoop.logger, UA_LOGCATEGORY_EVENTLOOP, "Stopping the EventLoop");

    /* Set to STOPPING to prevent "normal use" */
    *(UA_EventLoopState*)(uintptr_t)&el->cLoop.state = UA_EVENTLOOPSTATE_STOPPING;

    /* Run all delayed callbacks */
    processDelayed(el, NULL);

    /* Stop all event sources (asynchronous) */
    UA_EventSource *es = el->cLoop.eventSources;
    for(; es; es = es->next) {
        if(es->state == UA_EVENTSOURCESTATE_STARTING ||
           es->state == UA_EVENTSOURCESTATE_STARTED) {
            es->stop(es);
        }
    }

    /* Set to STOPPED if all EventSources are STOPPED */
    checkClosed(el);

    UA_UNLOCK(&el->elMutex);
}

UA_StatusCode
AsyncIOLoop_run(AsyncIOLoop *el, UA_UInt32 timeout) {
    /* If tearing down (inside tp_dealloc / GC), skip all Python calls.
     * Calling PyObject_CallMethod during GC can crash with coverage
     * instrumentation assertions or _PyType_Lookup debug assertions. */
    if(el->tearingDown || !el->pyLoop) {
        return UA_STATUSCODE_BADINTERNALERROR;
    }
    int running = 0;
    PyObject *r = PyObject_CallMethod(el->pyLoop, "is_running", NULL);
    if(r) { running = PyObject_IsTrue(r); Py_DECREF(r); }
    else { PyErr_Clear(); }
    int closed = 0;
    PyObject *c = PyObject_CallMethod(el->pyLoop, "is_closed", NULL);
    if(c) { closed = PyObject_IsTrue(c); Py_DECREF(c); }
    else { PyErr_Clear(); }
    if(closed || !running) {
        return UA_STATUSCODE_BADINTERNALERROR;
    }

    /* The asyncio event loop drives timers and I/O.  We only need to flush
     * delayed callbacks that were queued synchronously (e.g., during
     * run_shutdown) so that socket-close events propagate immediately. */
    processDelayed(el, NULL);
    return UA_STATUSCODE_GOOD;
}

static PyObject *safe_noop(PyObject *self, PyObject *args) { Py_RETURN_NONE; }
static PyMethodDef NoOpMethod = {"safe_noop", (PyCFunction)safe_noop, METH_NOARGS, ""};

static void
AsyncIOLoop_cancel(AsyncIOLoop *el) {
    PyObject *callback = PyCFunction_New(&NoOpMethod, NULL);
    if(!callback)
        return;
    PyObject *result = PyObject_CallMethod(el->pyLoop, "call_soon_threadsafe", "O", callback);
    if(!result)
        PyErr_Clear();
    Py_DECREF(callback);
    Py_XDECREF(result);
}

static UA_StatusCode
AsyncIOLoop_free(AsyncIOLoop *el) {
    UA_LOCK(&el->elMutex);

    /* Check if the EventLoop can be deleted */
    if(el->cLoop.state != UA_EVENTLOOPSTATE_STOPPED &&
       el->cLoop.state != UA_EVENTLOOPSTATE_FRESH) {
        UA_LOG_WARNING(el->cLoop.logger, UA_LOGCATEGORY_EVENTLOOP,
                       "Cannot delete a running EventLoop");
        UA_UNLOCK(&el->elMutex);
        return UA_STATUSCODE_BADINTERNALERROR;
    }

    /* Deregister and delete all the EventSources */
    while(el->cLoop.eventSources) {
        UA_EventSource *es = el->cLoop.eventSources;
        AsyncIOLoop_deregisterEventSource(el, es);
        es->free(es);
    }

    /* Disarm all pending timers.  Null timerHandle and le_prev BEFORE
     * Py_DECREF so that deleteTimer (which may run during Py_DECREF)
     * sees NULL and skips the LIST_REMOVE.
     *
     * We deliberately avoid PyObject_CallMethod(handle, "cancel") here
     * because this function may be called during GC (via tp_dealloc of
     * pyClient or pyServer).  Calling Python methods during GC can
     * crash (PyErr_Occurred assertion on debug builds, segfault on
     * 3.13 release builds).  Instead we set t->cb = NULL so that
     * executePyUATimer is a no-op if the handle still fires.
     *
     */
    PyUATimer *t, *t_tmp;
    LIST_FOREACH_SAFE(t, &el->timers, pointers, t_tmp) {
        LIST_REMOVE(t, pointers);
        t->pointers.le_prev = NULL;
        t->cb = NULL;   /* make executePyUATimer a no-op */
        t->el = NULL;
        if(t->timerHandle) {
            PyObject *handle = t->timerHandle;
            t->timerHandle = NULL;
            Py_DECREF(handle);
        }
    }

    /* Disarm all pending delayed timers (call_soon_threadsafe handles from
     * addDelayedCallback).  Same rationale as above. */
    LIST_FOREACH_SAFE(t, &el->delayedTimers, pointers, t_tmp) {
        LIST_REMOVE(t, pointers);
        t->pointers.le_prev = NULL;
        t->cb = NULL;
        t->el = NULL;
        if(t->timerHandle) {
            PyObject *handle = t->timerHandle;
            t->timerHandle = NULL;
            Py_DECREF(handle);
        }
    }

    Py_XDECREF(el->pyLoop);
    el->pyLoop = NULL;
    el->cLoop.logger->clear((UA_Logger*)el->cLoop.logger);

    // Clean up
    UA_KeyValueMap_clear(&el->cLoop.params);
    UA_UNLOCK(&el->elMutex);
    UA_LOCK_DESTROY(&el->elMutex);
    UA_free(el);
    return UA_STATUSCODE_GOOD;
}

int
AsyncIOEventLoop_initTypes(void) {
    if(PyUATimerType.tp_flags & Py_TPFLAGS_READY)
        return 0;
    return PyType_Ready(&PyUATimerType);
}

UA_EventLoop *
UA_EventLoop_new_AsyncIO(PyObject *pyLoop, PyObject *pyLog) {
    /* PyType_Ready was already called during module init */
    if(!(PyUATimerType.tp_flags & Py_TPFLAGS_READY)) {
        if(AsyncIOEventLoop_initTypes() < 0)
            return NULL;
    }

    // Allocate the EventLoop
    AsyncIOLoop *el = (AsyncIOLoop*)UA_calloc(1, sizeof(AsyncIOLoop));
    if(!el)
        return NULL;

    UA_LOCK_INIT(&el->elMutex);

    el->pyLoop = pyLoop;
    Py_INCREF(pyLoop); /* Strong reference — prevents use-after-free when
                        * subtype_dealloc clears __dict__ before tp_dealloc. */

    el->cLoop.logger = pyLogger(pyLog);

    el->cLoop.start = (UA_StatusCode (*)(UA_EventLoop*))AsyncIOLoop_start;
    el->cLoop.stop = (void (*)(UA_EventLoop*))AsyncIOLoop_stop;
    el->cLoop.free = (UA_StatusCode (*)(UA_EventLoop*))AsyncIOLoop_free;
    el->cLoop.run = (UA_StatusCode (*)(UA_EventLoop*, UA_UInt32))AsyncIOLoop_run;
    el->cLoop.cancel = (void (*)(UA_EventLoop*))AsyncIOLoop_cancel;

    el->cLoop.dateTime_now = (UA_DateTime (*)(UA_EventLoop *el))AsyncIOLoop_now;
    el->cLoop.dateTime_nowMonotonic = (UA_DateTime (*)(UA_EventLoop *el))AsyncIOLoop_nowMonotonic;
    el->cLoop.dateTime_localTimeUtcOffset = (UA_Int64 (*)(UA_EventLoop *el))AsyncIOLoop_localTimeUtcOffset;

    el->cLoop.nextTimer = AsyncIOLoop_nextTimer;
    el->cLoop.addTimer = AsyncIOLoop_addTimer;
    el->cLoop.modifyTimer = AsyncIOLoop_modifyTimer;;
    el->cLoop.removeTimer = AsyncIOLoop_removeTimer;
    el->cLoop.addDelayedCallback = AsyncIOLoop_addDelayedCallback;
    el->cLoop.removeDelayedCallback = AsyncIOLoop_removeDelayedCallback;

    el->cLoop.registerEventSource =
        (UA_StatusCode (*)(UA_EventLoop*, UA_EventSource*))
        AsyncIOLoop_registerEventSource;
    el->cLoop.deregisterEventSource =
        (UA_StatusCode (*)(UA_EventLoop*, UA_EventSource*))
        AsyncIOLoop_deregisterEventSource;

    el->cLoop.lock = (void (*)(UA_EventLoop *))AsyncIOLoop_lock;
    el->cLoop.unlock = (void (*)(UA_EventLoop *))AsyncIOLoop_unlock;

    /* Start timer IDs at 1.  open62541 uses callbackId == 0 as "no timer
     * registered" (e.g. Subscription.publishCallbackId).  If we hand out
     * id 0, removeTimer is never called for that timer. */
    el->timerIndex = 1;

    // Add TCP
    UA_ConnectionManager *tcpCM = UA_ConnectionManager_new_AsyncIO_TCP();
    AsyncIOLoop_registerEventSource(el, &tcpCM->eventSource);

    return &el->cLoop;
}
