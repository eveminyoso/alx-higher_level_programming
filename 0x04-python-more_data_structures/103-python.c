#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    if (PyList_Check(p)) {
        Py_ssize_t size = PyList_Size(p);
        PyObject *element;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

        for (Py_ssize_t i = 0; i < size; i++) {
            element = PyList_GetItem(p, i);
            printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
        }
    } else {
        fprintf(stderr, "Invalid List Object\n");
    }
}

void print_python_bytes(PyObject *p) {
    if (PyBytes_Check(p)) {
        Py_ssize_t size = PyBytes_Size(p);

        printf("[.] bytes object info\n");
        printf("  size: %ld\n", size);
        printf("  trying string: %s\n", PyBytes_AS_STRING(p));

        if (size < 10) {
            printf("  first %ld bytes: ", size);
        } else {
            printf("  first 10 bytes: ");
            size = 10;
        }

        for (Py_ssize_t i = 0; i < size; i++) {
            printf("%02x", (unsigned char)PyBytes_AS_STRING(p)[i]);
            if (i < size - 1) {
                printf(" ");
            }
        }
        printf("\n");
    } else {
        fprintf(stderr, "Invalid Bytes Object\n");
    }
}
