"""
    raise语法：raise 异常类名('异常信息')
"""

# print(123)
# raise ValueError('类型异常')
# print(456)
#rasie也可以放在except代码块中，可以重复引发异常；
try:
    print(1/0)
except:
    raise ZeroDivisionError('除数不能为0')
