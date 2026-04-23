# Copyright (c) 2026 o6 Automation GmbH
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import xml.etree.ElementTree as ET
import argparse


def parse_nodeset_for_enums(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    ns = {'ua': root.tag.split('}')[0].strip('{')}
    enums = []
    for datatype in root.findall('.//ua:UADataType', ns):
        definition = datatype.find('ua:Definition', ns)
        enum_values = []
        if definition is not None:
            for field in definition.findall('ua:Field', ns):
                value = field.get('Value')
                name = field.get('Name')
                if value is not None and name is not None:
                    enum_values.append((name, int(value)))
        if enum_values:
            enums.append((datatype.get('BrowseName'), enum_values))
    return enums


def print_enum_overview(enums):
    for enum_name, members in enums:
        print(f"Enum: {enum_name}")
        for name, value in members:
            print(f"  {name} = {value}")


def generate_c_enum_code(enums):
    c_code = []
    for enum_name, members in enums:
        safe_name = enum_name.replace(':', '_').replace('.', '_')
        c_code.append(f'// Enum: {enum_name}')
        c_code.append(f'''static void create_{safe_name}_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare) {{
    PyObject *enum_dict = NULL, *enum_class = NULL, *args, *kwargs, *keep, *flag_boundary;
    enum_dict = PyObject_CallFunctionObjArgs(prepare, PyUnicode_FromString("{safe_name}"), bases, NULL);
    if(!enum_dict) goto error;
    if(setItem(enum_dict, PyUnicode_FromString("__module__"), PyUnicode_FromString("o6.types")) < 0) goto error;''')
        for i, (name, value) in enumerate(members):
            c_code.append(f'    setItem(enum_dict, PyUnicode_FromString("{name.upper()}"), PyLong_FromLong({value}));')
        c_code.append(f'''    flag_boundary = PyObject_GetAttrString(enum_module, "FlagBoundary"); if(!flag_boundary) goto error;
    keep = PyObject_GetAttrString(flag_boundary, "KEEP"); if(!keep) goto error;
    args = PyTuple_Pack(3, PyUnicode_FromString("{safe_name}"), bases, enum_dict); if(!args) goto error;
    bases = NULL; enum_dict = NULL; // References taken over py PyTuple_Pack
    kwargs = PyDict_New(); if(!kwargs) goto error;
    if(PyDict_SetItemString(kwargs, "boundary", keep) < 0) goto error;
    enum_class = PyObject_Call(EnumClass, args, kwargs); if(!enum_class) goto error;
    PyModule_AddObject(module, "{safe_name}", enum_class);
    enum_class = NULL; // reference taken by PyModule_AddObject
  error:
    PyErr_Print();
    Py_XDECREF(enum_dict);
    Py_XDECREF(args);
    Py_XDECREF(kwargs);
    Py_XDECREF(flag_boundary);
    Py_XDECREF(keep);
    Py_XDECREF(enum_class);
}}''')
    return '\n'.join(c_code)


def generate_full_c_file(enums):
    c_code = []
    c_code.append('#include <Python.h>')
    c_code.append('#include <setobject.h>')
    c_code.append('')
    c_code.append('// Forward declarations for enum creation functions')
    for enum_name, _ in enums:
        safe_name = enum_name.replace(':', '_').replace('.', '_')
        c_code.append(f'static void create_{safe_name}_enum(PyObject *module, PyObject *enum_module, PyObject *EnumClass, PyObject *bases, PyObject *prepare);')
    c_code.append('')
    c_code.append('''
// add elements to the dictionary and release key+value
// for inline operations
static int
setItem(PyObject *dct, PyObject *key, PyObject *value) {
    int res = -1;
    if(key && value)
        res = PyObject_SetItem(dct, key, value);
    Py_XDECREF(key);
    Py_XDECREF(value);
    return res;
}

// Overload __call__ for enums to allow initialization without a value (default = 0)
static PyObject *
PyUAEnum_call(PyObject *cls, PyObject *args, PyObject *kwds) {
    PyObject *call_args = NULL;
    if(PyTuple_Size(args) == 0 && (!kwds || PyDict_Size(kwds) == 0)) {
        PyObject *zero = PyLong_FromLong(0);
        if(!zero)
            return NULL;
        call_args = PyTuple_Pack(1, zero);
        if(!call_args) {
            Py_DECREF(zero);
            return NULL;
        }
        args = call_args;
    }

    PyTypeObject *meta_type = Py_TYPE(cls);
    if(!meta_type->tp_base || !meta_type->tp_base->tp_base ||
       !meta_type->tp_base->tp_base->tp_call) {
        PyErr_SetString(PyExc_TypeError, "Base tp_call not found");
        Py_XDECREF(call_args);
        return NULL;
    }

    PyObject *result = meta_type->tp_base->tp_base->tp_call(cls, args, kwds);
    Py_XDECREF(call_args);
    return result;
}

static PyObject *
PyUAEnum_iter(PyObject *cls) {
    PyObject *members = PyObject_GetAttrString(cls, "__members__");
    if (!members) return NULL;
    PyObject *values = PyMapping_Values(members);
    Py_DECREF(members);
    if(!values) return NULL;
    PyObject *it = PyObject_GetIter(values);
    Py_DECREF(values);
    return it;
}

static PyObject *
PyUAEnum_dir(PyObject *cls, PyObject *Py_UNUSED(ignored)) {
    PyTypeObject *enum_meta = Py_TYPE(cls)->tp_base;
    if(!enum_meta) return NULL;

    PyObject *dir_func = PyObject_GetAttrString((PyObject*)enum_meta, "__dir__");
    if(!dir_func) return NULL;

    PyObject *super_dir = PyObject_CallFunctionObjArgs(dir_func, cls, NULL);
    Py_DECREF(dir_func);
    if(!super_dir) {
        PyErr_Print();
        return NULL;
    }

    PyObject *members_prop = PyObject_GetAttrString(cls, "__members__");
    if(!members_prop) {
        PyErr_Print();
        Py_DECREF(super_dir);
        return NULL;
    }

    PyObject *member_names = PyMapping_Keys(members_prop);
    Py_DECREF(members_prop);
    if(!member_names) {
        PyErr_Print();
        Py_DECREF(super_dir);
        return NULL;
    }

    PyObject *set = PySet_New(super_dir);
    Py_DECREF(super_dir);
    if(!set) {
        PyErr_Print();
        Py_DECREF(member_names);
        return NULL;
    }

    if(PyObject_CallMethod(set, "update", "O", member_names) == NULL) {
        PyErr_Print();
        Py_DECREF(set);
        Py_DECREF(member_names);
        return NULL;
    }

    Py_DECREF(member_names);
    return PySequence_List(set);
}

static PyMethodDef PyUAEnum_methods[] = {
    {"__dir__", (PyCFunction)PyUAEnum_dir, METH_NOARGS, "Custom __dir__"},
    {NULL, NULL, 0, NULL}
};

 static PyType_Slot PyUAEnum_slots[] = {
    {Py_tp_call, PyUAEnum_call},
    {Py_tp_iter, PyUAEnum_iter},
    {Py_tp_methods, PyUAEnum_methods},
    {0, NULL}
};

static PyType_Spec PyUAEnum_spec = {
    .name = "o6.types._Enum",
    .basicsize = 0, // set dynamically
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .slots = PyUAEnum_slots,
};
''')
    c_code.append('// Function to create all enums and add them to the module')
    c_code.append('''void create_all_enums(PyObject *module) {
    PyObject *enum_module = PyImport_ImportModule("enum");
    if(!enum_module) return;
    PyObject *EnumMeta = NULL, *IntFlag = NULL, *bases = NULL,
             *UAEnum_Type = NULL, *prepare = NULL;
    EnumMeta = PyObject_GetAttrString(enum_module, "EnumMeta");
    IntFlag = PyObject_GetAttrString(enum_module, "IntFlag");
    if(!EnumMeta || !IntFlag) goto done;
    bases = PyTuple_Pack(1, EnumMeta);
    if(!bases) goto done;
    Py_INCREF(enum_module); // Counter-act the reference stolen in PyTuple_Pack
    PyUAEnum_spec.basicsize = ((PyTypeObject *)EnumMeta)->tp_basicsize;
    UAEnum_Type = PyType_FromSpecWithBases(&PyUAEnum_spec, bases);
    if(!UAEnum_Type) goto done;
    if(PyModule_AddObject(module, "_Enum", UAEnum_Type) < 0) goto done;
    Py_INCREF(UAEnum_Type); // Counter the reference stolen in PyModule_AddObject
    Py_DECREF(bases);
    bases = PyTuple_Pack(1, IntFlag);
    if(!bases) goto done;
    Py_INCREF(IntFlag); // Counter-act the reference stolen in PyTuple_Pack
    prepare = PyObject_GetAttrString(EnumMeta, "__prepare__");
    if(!prepare) goto done;''')
    for enum_name, _ in enums:
        safe_name = enum_name.replace(':', '_').replace('.', '_')
        c_code.append(f'    create_{safe_name}_enum(module, enum_module, UAEnum_Type, bases, prepare);')
    c_code.append('''done:
    Py_DECREF(enum_module);
    Py_XDECREF(EnumMeta);
    Py_XDECREF(IntFlag);
    Py_XDECREF(bases);
    Py_XDECREF(UAEnum_Type);
    Py_XDECREF(prepare);
}''')
    # Add all enum creation functions
    c_code.append(generate_c_enum_code(enums))
    return '\n'.join(c_code)


def generate_c_enum_header(enums):
    h_code = []
    h_code.append('#ifndef SRC_CMODULE_ENUM_H_')
    h_code.append('#define SRC_CMODULE_ENUM_H_')
    h_code.append('')
    h_code.append('#include <Python.h>')
    h_code.append('')
    h_code.append('// Forward declaration for function to add all enums')
    h_code.append('void create_all_enums(PyObject *module);')
    h_code.append('')
    h_code.append('#endif // SRC_CMODULE_ENUM_H_')
    return '\n'.join(h_code)


def main():
    parser = argparse.ArgumentParser(description="Parse an OPC UA NodeSet2 XML file for Enum DataTypes and generate C code.")
    parser.add_argument("xml_file", help="Path to the NodeSet2.xml file")
    parser.add_argument("output_dir", type=str, help="Directory where the generated C and header files will be created")
    args = parser.parse_args()
    enums = parse_nodeset_for_enums(args.xml_file)
    import os
    output_path = os.path.join(args.output_dir, "src_cmodule_enum.c")
    header_path = os.path.join(args.output_dir, "src_cmodule_enum.h")
    c_code = generate_full_c_file(enums)
    h_code = generate_c_enum_header(enums)
    with open(output_path, 'w') as f:
        f.write(c_code)
    with open(header_path, 'w') as f:
        f.write(h_code)
    print(f"C code written to {output_path}")
    print(f"Header written to {header_path}")


if __name__ == "__main__":
    main()
