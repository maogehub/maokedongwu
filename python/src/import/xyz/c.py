import os
import sys
current_dir=os.path.dirname(os.path.realpath(__file__))
parent_dir=os.path.dirname(current_dir)
sys.path.insert(0,parent_dir)
import a
a.hello()
b=a.Hello()
b.hello()
