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
