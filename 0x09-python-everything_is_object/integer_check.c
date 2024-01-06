#include <Python.h>

void print_integer_info(PyObject *obj) {
   if (!PyLong_Check(obj)) {
       printf("Not an integer.\n");
       return;
   }

   Py_ssize_t size = PyLong_AsSsize_t(obj);
   printf("Integer value: %ld\n", size);
}
