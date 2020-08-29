"""
    open('文件路径'[,'读写模式'][,encoding='UTF-8'])
"""
f = open('./test_file.txt','r') #读模式
f = open('./test_file.txt','w') #写模式
f = open('./test_file.txt','a') #追加模式
f = open('./test_file.txt','wt') #字符写模式
f = open('./test_file.txt','wb') #二进制写模式

f.close()
#此时如果没有报错，就说明是正确的；
