a = {1:'one',2:'two',3:'three'}
c = a
b = a.copy() #如果用copy()就变成另一个字典；
#id()随机获取一个字典id，如果id值一样，说明是同一个字典；
print(id(a))
print(id(b)) #以上两种id值不一样
print(id(c)) #这个id值跟a一样；
