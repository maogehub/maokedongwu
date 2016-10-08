#include <Python.h>
static PyObject * add(PyObject *self, PyObject *args)
{
    int x, y;
    if (!PyArg_ParseTuple(args, "ii", &x, &y)) 
    {
        return NULL;
    }
    return Py_BuildValue("i", x+y);
}

static PyMethodDef AddMethods[] = {
    {"add", add, METH_VARARGS, "add 2 numbers"},
    {NULL, NULL, 0, NULL}
};

int initadd(void)
{
    (void) Py_InitModule("add", AddMethods);
}

int main(int argc, char *argv[])
{
    Py_SetProgramName(argv[0]);
    Py_Initialize();
    initadd();
}
