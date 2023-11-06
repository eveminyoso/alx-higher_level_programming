#include <Python.h>
/**
 *print_python_list_info - uses python C API to extract list's details
 *@p:pointer to python list object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *obj;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
