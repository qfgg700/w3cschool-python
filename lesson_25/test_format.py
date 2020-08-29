"""
    format语法："{位置参数|关键字参数}....".format(位置参数|关键字参数='值'....)
"""
#第一种：位置参数
print("{0},{1},{2}".format('1','2','3')) #1,2,3
#第二种：关键字参数
print("{a},{b},{c}".format(a='a',b='b',c='c')) #a,b,c
#第三种：位置参数和关键字参数混合
print('{0},{a},{b}'.format('1',a='2',b='3')) #1,2,3
#语法错误，如果混合，位置参数一定要放在关键字参数的前面；
# print('{a},{0},{b}'.format(a='2','1',b='3'))
#第四种：位置参数不写
print("{},{},{}".format('one','two','three')) #one,two,three
#第五种：设置指定位置，可以多次使用；
print("{a} {b} {a}".format(a='hello',b='and')) #hello and hello
#第六种：使用字典格式化
person = {"name":"W3Cschool","age":5,'sex':'18'}
print("My name is {name} . I am {age} years old {sex}.".format(**person)) #My name is W3Cschool . I am 5 years old .
#第七种：通过列表格式化；
stu = ["W3Cschool","linux","MySQL","Python"]
print("My name is {0[0]} , I love {0[3]} !".format(stu)) #My name is W3Cschool , I love Python !
