dict1 = {}
dict1 = dict1.fromkeys(range(5),'小明')
# print(dict1.get(5)) #输出：None找不到对应的键值；
# print(dict1.get(3,'找不到的结果就输出这个')) #返回小红，记得不是往字典里面加 希望找不到的时候，能输出一个值，第二个参数就可以使用了
print(5 in dict1) #判断5这个键值，在字典中是否存在；
print(5 not in dict1) #跟上面刚好相反；
# #遍历字典；
for each in dict1:
    print(dict1.get(each))