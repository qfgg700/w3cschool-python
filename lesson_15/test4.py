name = '小明' #这个就是全局变量；
def fun():
    age = 18 #在函数内叫局部变量
    return name,age
print(fun())
print("===============================")
a = 100
def test():
    global a #声明此时要调用的a变量是全局变量的a;
    a = a + 20
    print(a) #如果此时要输出全局变量a的值，怎么办？
test()