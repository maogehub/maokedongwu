# Import

平时聊天的时候，遇到不少人问关于 python import 的问题。

这里简单介绍一下python的import

这里的代码，都在 [import](../src/import) 目录下

## 同目录下的 import
同目录下的 import 应该很好理解

在一个目录下，有一个文件 a.py 里面定义了function或者class。然后在一个叫做b.py的文件中，去调用a.py中的东西

[a.py] (../src/import/a.py)

~~~python
def hello():
    print "hello function"
    
class Hello(object):
    def hello(self):
        print "hello class"
~~~

同目录内的 [b.py] (../src/import/b.py)

~~~python
import a
a.hello()   #这里调用 a.py 中的 hello funciton
b=a.Hello() #这里调用 a.py 中的 Hello class
b.hello()
~~~

## 下级目录中的 import
下级目录是说，你在当前文件夹内，有个xyz的子文件夹。里面有个a.py

这个时候，你在这个子目录中，就要有一个 **__init__.py** 文件。不文件本身可以是空的，什么都没有。但是这个会告诉python，这个文件夹内是python的模组

```
├── a.py
├── b.py
├── c.py
└── xyz
    ├── __init__.py
    └── a.py
```
我们这里c.py希望去调用xyz目录下的a.py

[xyz/a.py](../src/import/xyz/a.py)

~~~python
def hello():
    print "hello function in xyz"

class Hello(object):
    def hello(self):
        print "hello class in xyz"
~~~

[c.py](../src/import/c.py)

~~~python
from xyz import a
a.hello()
b=a.Hello()
b.hello()
~~~

## 从上级目录 import
在当前目录下，去import上面的目录中的东西

```
├── a.py
├── b.py
├── c.py
└── xyz
    ├── __init__.py
    ├── a.py
    └── b.py
```

我们这次，是要从 xyz中的b.py去import 最上面的 a.py
因为上级目录并不在我们的path中，那么一般有两个做法。

做法1，直接用 **“../”** 这样的路径，放在sys的path中

[xyz/b.py](../src/import/xyz/b.py)

~~~python
import sys
sys.path.append('../')
import a
a.hello()
b=a.Hello()
b.hello()
~~~

做法2，找到正确的路径

[xyz/c.py](../src/import/xyz/c.py)

~~~python
import os
import sys
current_dir=os.path.dirname(os.path.realpath(__file__))
parent_dir=os.path.dirname(current_dir)
sys.path.insert(0,parent_dir)
import a
a.hello()
b=a.Hello()
b.hello()
~~~

## 从上级目录中的其他目录下 import

```
├── a.py
├── b.py
├── c.py
├── xxx
│   ├── __init__.py
│   └── a.py
├── xyz
│   ├── __init__.py
│   ├── a.py
│   ├── b.py
│   └── c.py
└── zzz
    └── b.py
```

在目录zzz中的b.py下，去import xxx中的a.py跟xyz中的a.py

[zzz/b.py](../src/import/zzz/b.py)

~~~python
import os
import sys
current_dir=os.path.dirname(os.path.realpath(__file__))
parent_dir=os.path.dirname(current_dir)
sys.path.insert(0,parent_dir)
from xyz import a as xyz_a
from xxx import a as xxx_a
xyz_a.hello()
b=xyz_a.Hello()
b.hello()
xxx_a.hello()
b=xxx_a.Hello()
b.hello()
~~~

