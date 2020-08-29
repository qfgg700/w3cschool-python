"""
    元组语法1：
        变量名 = (元素1，元素2....)
    元组语法2：
        变量名 = 元素1，元素2.....
    特点：python中唯一不可变的集合；
"""
tuple1 = (1,2,3,4)
print(tuple1)
print(tuple1[2]) #输出3
# tuple1[3] = 100 #抛出TypeError异常，不可变；
tuple2 = 'one','two','three'
print(type(tuple2)) #<class 'tuple'>
#可以用for循环来遍历；
for each in tuple2:
    print(each)