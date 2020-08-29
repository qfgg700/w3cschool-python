#收集参数：*变量名
def test(*a,b):
    for each in a:
        print(each)
    print(b)
test(1,2,3,b=4) #如果有第二个参数，记得变量名要写上去；