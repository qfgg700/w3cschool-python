#语法1：from [文件夹].模块名 import 方法名，变量名
#语法2：from [文件夹].模块名 import * 不建议采用这种；
from lesson_16.test.py_test import fun,name
fun()
print(name)
#此时可以调用py_test.py里面的方法和变量；