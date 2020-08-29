# print(None) #None null 缺值
# print(None==None) #True
# print(None==0) #False，None有自己的类型，值为None，不是0；
# print(None==False) #这个也是同理
# print(None=="") #这个也是同理
def fun():
    a = 123
    return
a = fun()
print(a) #此时返回None，无return返回None常量值；