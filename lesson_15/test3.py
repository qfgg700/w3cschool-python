def f1():
    return 'hello'
def f2():
    return 'world'
def fun(f1,f2):
    return f1+f2
a = f1()
b = f2()
print(fun(a,b))# helloworld
print(fun(f1(),f2()))# helloworld
