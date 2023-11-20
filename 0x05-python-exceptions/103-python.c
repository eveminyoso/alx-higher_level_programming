#include <Python.h>
/**
 *print_python_list - info of a list
 *@p:pointer to object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i;
	const char *typeName;

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);
	for (i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);

		typeName = Py_TYPE(item)->tp_name;

		printf("Element %ld: %s\n", i, typeName);
	}
}
/**
 *print_python_bytes - byte codes
 *@p:pointer to object
 *
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i;

	printf("[.] Python bytes info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("[.] Size: %ld\n", PyBytes_Size(p));
	Py_ssize_t toPrint = size < 10 ? size : 10;

	for (i = 0; i < toPrint; ++i)
	{
		printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
		if (i < toPrint - 1)
			printf(" ");
	}
	printf("\n");
}
/**
 *print_python_float - float info
 *@p:poniter to object
 */
void print_python_float(PyObject *p)
{
	printf("[.] Python float info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	printf("[.] Value: %f\n", PyFloat_AsDouble(p));
}
/**
 *main - gatepass
 *Return:Exit value 0
 *
 */
int main(void)
{
	PyObject *bytes = PyBytes_FromStringAndSize("Python", 6);
	PyObject *floating = PyFloat_FromDouble(98.765);

	Py_Initialize();
	print_python_list(list);
	print_python_bytes(bytes);
	print_python_float(floating);
	Py_DECREF(list);
	Py_DECREF(bytes);
	Py_DECREF(floating);
	Py_Finalize();
	return (0);
}
