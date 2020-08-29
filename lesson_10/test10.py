list = [1,2,3,4,5,2]
print(max(list)) #返回具有最大值的列表元素
print(min(list)) #返回具有最小值的列表元素
print(list.count(2)) #返回一个元素在一个列表中出现的次数 2
list.remove(3) #从列表中删除一个元素
print(list) #我们发现3的值被删除了；[1, 2, 4, 5, 2]
list.reverse() #颠倒列表中的元素的顺序
print(list) #[2, 5, 4, 2, 1] 反转过来了