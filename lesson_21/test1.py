try:
    f = open('test_file.txt','r',encoding='UTF-8')
    print(f.read())
finally:
    f.close() #不管怎么样都会执行；