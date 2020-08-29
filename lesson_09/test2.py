b = 1
# while b==1:
#     print('hello')
#     break
#这个循环要是没有break，则陷入死循环；
while b<=10:
    print(b)
    while True:
        break #这边结束的循环是内部的循环；
    b = b + 1