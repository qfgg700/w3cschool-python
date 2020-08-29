# f = open('./test_file.txt','w',encoding='UTF-8')
# # str_content = f.write('这是一个新的知识点') #写入成功；
# seq = ['hello','world','123']
# str_content = f.writelines(seq) #其实就是把列表中所有的字符串按顺序写入文件；
# f.close()
ff = open('./test_file.txt','a',encoding='UTF-8')
ff.write('后文本后面添加内容!') #追加模式
ff.close()
