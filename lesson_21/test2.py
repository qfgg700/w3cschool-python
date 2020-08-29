"""
    with作用：针对文件操作，可以大大减少代码量，同时也不用担心文件关闭的问题；
    with语法：with open() as 临时变量名：<文件处理>
"""
# try:
#     f = open('test_file.txt','r',encoding='UTF-8')
#     print(f.read())
# except:
#     print("文件出问题了")
# finally:
#     f.close()
#用with语句来改装；
try:
    with open('test_file.txt','r',encoding='UTF-8') as f:
        print(f.read())
except:
    print('文件出问题了')