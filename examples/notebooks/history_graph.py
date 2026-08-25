#!/usr/bin/env python
# coding: utf-8

# ## Plot history of a variable
#
# Use Matplotlib to visualize a variable history
#
# 1. Set config of the server to allow historizing
# 2. Create Variable and change it
# 3. Read history
# 4. Plot

# In[ ]:


get_ipython().run_line_magic("pip", "install matplotlib -q")
from o6 import Client, StatusCodeError, types, Server
import datetime

s = Server(port=4840)
c = Client("opc.tcp://localhost:4840")


# In[ ]:


# enable historizing
s.config.setHistoryDatabase()
s.register_historizing("ns=1;s=Temperature")
temp = s.addVariable(
    "Temperature", s.objectsNode, 15.0, nodeId="ns=1;s=Temperature", historizing=True
)


# In[ ]:


s.start()
await c.connect()


# ### Add subscription to a variable
#
# The new values are printed above when ```Temperature``` is changed

# In[ ]:


sub = await c.createSubscription(publishingInterval=500.0)
central = await c.monitor(
    "ns=1;s=Temperature",
    lambda value: print(f"value: {value}"),
    samplingInterval=500.0,
    subscription=sub,
)

import random
import time

for i in range(25):
    value = random.randrange(10, 25, 1)
    await c.write("ns=1;s=Temperature", types.Double(value))
    time.sleep(0.5)


# ### Request the History of the Variable Temperature

# In[ ]:


now = datetime.datetime.now(tz=datetime.timezone.utc)
earlier = datetime.datetime.now(tz=datetime.timezone.utc) - datetime.timedelta(hours=1)

history = await c.historyRead("ns=1;s=Temperature", earlier, now)


# ### Basic matplotlib graph

# In[ ]:


import matplotlib.pyplot as plt

values = [dv.value for dv in history.dataValues]

plt.plot(values, marker="o")
plt.grid(True)
plt.title("Temperature Flactuations")
plt.show()


# In[ ]:


await c.disconnect()
s.stop()
