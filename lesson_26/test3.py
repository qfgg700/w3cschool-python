"""
all 列表中所有值均为True时，结果为True，否则结果为False
any 列表中只要有一个为True，结果为True，反之结果为False
enumerate 函数可以用来同时迭代列表的键和值
"""
nums = [55, 44, 33, 22, 11]
if all([i > 5 for i in nums]):
   print("All larger than 5")
if any([i % 2 == 0 for i in nums]):
   print("At least one is even")
#输出nums列表的键和值；
for v in enumerate(nums):
   print(v)
# (0, 55)
# (1, 44)
# (2, 33)
# (3, 22)
# (4, 11)