# for each in range(0,3):
#     print('@')
# for each in range(0,4):
#     print('*')
# for each in range(0,5):
#     print('*')
# 语法：def 函数名(形参1，形参2....)： 《代码块》调用方式：函数名(实参1，实参2...)
def print_start(k,str):
    for each in range(0,k):
        print(str+"hello")
print_start(3,'@') #此时的3就是实参
print_start(4,'*')
print_start(5,'*')
#很明显，有了函数效果更好，代码更易于维护；