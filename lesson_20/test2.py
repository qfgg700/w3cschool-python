f = open('./test_file.txt','r',encoding='UTF-8')
# content = f.read() #不给参数，表示读取文本中所有的信息；
# content = f.read(5) #表示读取5个字符；中文也算一个；
# content = f.read(-5) #如果是负数，也表示读取所有信息；
# f.readline() #跳过第一行；
# content = f.readline()
# content = f.readlines() #每一行的内容为列表中的一个元素；
# f.seek(5,0) #表示从文本内容第6个字符开始
# content = f.read(5) #读取5个字符；
# print(content)
# print(f.tell()) #返回当前文件的位置；
#用for循环来遍历；
for each in f:
    print(each) #每次读取一行；

f.close()