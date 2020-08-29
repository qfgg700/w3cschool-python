#语法1：import 模块名 as 别名
#语法2：from 模块名 import 变量名/函数 as 别名
import math as m
print(m.sqrt(16))
from lesson_16.test.py_test import fun as f
f() #对fun()方法取别名；