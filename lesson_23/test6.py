a = {'name':'黄老师'}
b = a
print(b) #有值
a = {}
print(a) #空值
print(b) #还是有值；
print("=========================")
a = {'name':'黄老师2'}
b = a
a.clear()
print(a)
print(b) #这两个输出都为空；