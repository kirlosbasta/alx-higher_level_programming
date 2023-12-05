#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p);

/**
 * print_python_list_info - print some basic info about a list
 * @p: pointer to list object
 *
 * Description: print the size of the list and the number of allocation
 * of each element and the index of the element and it's corrisponding type
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size;
	Py_ssize_t num_alloc;
	PyObject *item;
	PyTypeObject *type;
	int i;

	if (PyList_Check(p))
	{
		list_size = PyList_Size(p);
		num_alloc = ((PyListObject *)p)->allocated;
		printf("[*] Size of the Python List = %ld\n", list_size);
		printf("[*] Allocated = %ld\n", num_alloc);
		if (list_size > 0)
		{
			for (i = 0; i < list_size; i++)
			{
				item = PyList_GET_ITEM(p, i);
				type = Py_TYPE(item);
				printf("Element %d: %s\n", i, type->tp_name);
			}
		}
	}
}
