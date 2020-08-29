try:
    # print(1/0)
    name = '小明'
    print(name)
except ZeroDivisionError as e:
    print('错误信息：'+str(e))
finally: #不管怎么样，它一定有输出；
    print('哈哈，还是有输出')