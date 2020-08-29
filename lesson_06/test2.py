a = 1
b = 2
c = 2
d = 'ab'
e = "bc"
print(a>=b) #False
print(a<=c) #True 1<=2小于和等于只要有一个条件满足即为True
#False 'ab'>='bc' 比较第一个字母，很明显b排在a后面，所以后面不会再比，除非一样再会继续比
print(d>=e)
#True 同上
print(d<=e)