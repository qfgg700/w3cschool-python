"""
列表推导语法：[表达式1 for k in L if 表达式2]
备注：list的元素由每一个表达式1组成，if语句用于过滤，可以省略；
执行顺序：for>【表达式2】>表达式1
"""
# list = range(5)
# cubes = []
# for num in list:
#     cubes.append(num ** 3)
# print(cubes)
# #上面的代码可以简写成这样：
# list = [i**3 for i in range(5)]
# print(list) #这两个结果是一样的；
# #执行顺序先for后if最后i**2
# evens=[i**2 for i in range(10) if i**2 % 2 == 0]
# print(evens)
even = [2*i for i in range(10**100)]
print(even)