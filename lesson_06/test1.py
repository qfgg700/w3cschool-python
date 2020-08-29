# b = True
# c = False
# print(b,c,"布尔类型是什么")
#可以通过,逗号来同时输出N个变量或者分隔都可
# a = 1
# b = "2"
# c = "1"
# d = "2"
# print(a==b) #这个很明显不相等；
# print(a==c) #这两个虽然值是一样的，但类型不一样，所以也是False
# print(b==d) #这两个就相等了；
# print("--------------------------")
# a = 1
# b = 2
# c = "2"
# print(a!=b) #两边不相等，返回True
# print(b!=c) #两边值是一样的，但类型不一样，所以返回True
# print("-----------------------------")
# a = 1
b = 2
c = '1'
d = 2.0
# print(a>b) #False
# print(b<=d) #True
e = '123'
ee = '23'
print(e>ee) #1>2
print(b<c) #此时报TypeError错，<、>号两边不能有非整数或浮点数出现；
print(b>d) #False