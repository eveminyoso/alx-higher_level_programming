#include <Python.h>
/**
 *print_python_string -  prints Python strings
 *@p:pointer to python object
 */
void print_python_string(PyObject *p)
{
	if (PyUnicode_Check(p))
	{
		printf("[.] string object info\n");
		printf("  type: compact unicode object\n");
		printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
		printf("  value: %s\n", PyUnicode_AsUTF8(p));
	}
	else if (PyBytes_Check(p))
	{
		printf("[.] string object info\n");
		printf("  type: compact bytes object\n");
		printf("  length: %ld\n", PyBytes_GET_SIZE(p));
		printf("  value: %s\n", PyBytes_AsString(p));
	}
	else
	{
		PyErr_SetString(PyExc_TypeError, "Object is not a valid string");
		PyErr_Print();
	}
}
/**
 *main -  prints Python strings
 *Return:Exit value 0
 */
int main(void)
{
	Py_Initialize();
	PyObject *byteString = PyBytes_FromString("The spoon does not exist");

	print_python_string(unicodeString);

	print_python_string(byteString);

	Py_XDECREF(unicodeString);
	Py_XDECREF(byteString);
	Py_Finalize();
	return (0);
}
