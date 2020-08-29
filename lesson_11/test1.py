"""
range(n)表示从[0,n-1]
range(n,m)表示从[n,m-1]
range(n,m,k)表示从[n,m-1]之间，以k值为步长
"""
#通过list()函数来转换成列表；
b = list(range(10))
print(b) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0,10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0,10,2))) #[0, 2, 4, 6, 8]
print(list(range(0,10,2.5))) #报错，必须是整数