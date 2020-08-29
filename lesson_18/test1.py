"""
ModuleNotFoundError: 无法找到模块；
IndexError: 下标索引超出序列边界;
NameError: 使用一个还未赋予对象的变量;
SyntaxError: 代码逻辑语法出错，不能执行;
TypeError: 传入的对象类型与要求不符;
ValueError: 传入一个不被期望的值，即使类型正确。
KeyError： 试图访问你字典里不存在的键。
IOError： 输入输出异常。
"""
# import xx #ModuleNotFoundError: 无法找到模块;
# list = [1,2,3]
# print(list[3])  #IndexError: 下标索引超出序列边界;
# print(num)  #NameError: 使用一个还未赋予对象的变量;
# print 'I love python'  #SyntaxError: 代码逻辑语法出错，不能执行;
# print(type()) #TypeError: 传入的对象类型与要求不符;
# print(int('a'))  #ValueError: 传入一个不被期望的值，即使类型正确。
my_dict = {'one':1}
print(my_dict[2])  #KeyError： 试图访问你字典里不存在的键。
