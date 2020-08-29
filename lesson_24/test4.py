list1 = [1,3,2,4]
list2 = list1[:] #此时做分片效果，开辟新的存储空间；
print(list2) #[1, 3, 2, 4]
list3 = list1 #在同一个存储空间
print(list3) #此时输出结果一样；
print("==============================")
list1.sort()
print(list2) #list2的值还是[1, 3, 2, 4]不变；
print(list3) #list3的值此时跟list1变化[1, 2, 3, 4]