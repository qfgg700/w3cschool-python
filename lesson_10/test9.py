#index()返回指定元素在列表中的索引值；
list = [1,2,3,4]
print(list.index(2,0)) #1 返回2元素所对应的索引值；
print(list.index(2,1))#1 表示从第2个开始找；
print(list.index(2,2))#报ValueError错，表示从第3个开始找，很明显没有