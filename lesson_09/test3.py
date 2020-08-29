a = 0
while a<10:
    a = a + 1 #a = 1 2
    if a % 2 == 0:
        continue #跳过本次循环，继续下一次循环；即它后面的代码本次不执行；
    print(a) #1 3 5 7 9
