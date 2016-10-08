# Python 调用 C 语言库
python 跟 c 语言之间可以很容易的结合应用。python 的官方文档中也写得很清楚，并且给了例子。但是还是常常会遇到人问这个问题的。这就来说一下。[官方文档](https://docs.python.org/2/extending/extending.html)

python调用c语言的库有两种方法，一个是直接用python的ctype做调用，另外一个是，写c的时候，写入python的接口

## python ctype 调用 c 的 lib

[add.c](../src/c/ctype/add.c) 这个是一个简单的c funciton，我们定义一个叫做add的函数，允许输入两个整数 x 跟 y，返回 x+y

~~~c
int add(int x, int y)
{
    return x+y;
}
~~~

用 gcc 编辑，作出动态的shared library 

~~~bash
gcc -c add.c
gcc -shared -o add.so add.o
~~~

这个时候，我们会产生一个叫做 add.so 的文件

python可以直接用ctype去调用

[test.py](../src/c/ctype/test.py)

~~~python
#!/usr/bin/python
import ctypes
lib=ctypes.cdll.LoadLibrary("add.so")
print lib.add(10,15)
~~~

ctype 的方式，可以调用 “任意” 系统中的 c 的库。不过用ctype的时候，你要对本身你所调用的库的interface是需要有个了解。另外，如果c中的function是有pointer，callback等等，都需要你做额外的处理。官方文档中对于这些都有介绍

## 直接在 C 中定义 python 接口

也可以直接在 C 中去定义 python 的接口，例如我们用的很多python模组是c写的，接口就是直接在c中定义了的


[add.c](../src/c/interface/add.c) 仍然是上面的那个add的function，但是这次我们定义了python接口，所以python可以直接调用

~~~c
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
~~~

用 gcc 编辑，作出动态的shared library. 因为我们需要 include Python.h 并且link到python的lib，所以这个build步骤，就根据你的系统，用什么版本的python，会有差别。我个人平时都是用苹果，桌面有一个fedora 22的机器。所以下面的build步骤，是在我的苹果跟fedora中的环境下

~~~bash
if [[ $(uname) == "Darwin" ]]
then
    #osx build 
    gcc -I /Library/Frameworks/Python.framework/Versions/2.7/include/python2.7/ -c add.c 
    gcc -shared -lpython -o add.so add.o
else 
    #linux (fedora) build 
    gcc -I /usr/include/python2.7 -fPIC -c add.c 
    gcc -shared -o add.so add.o
fi
~~~

[test.py](../src/c/interface/test.py) 使用起来，就跟你使用普通的python模组没有任何区别了

~~~python
#!/usr/bin/python
import add
print add.add(10,15)
~~~
