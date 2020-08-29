list_fh = ['+','-','*','/','%','//']
while True:
    print("=========欢迎进入简易计算器=================")
    print("1、简易计算器；")
    print("2、退出系统；(任意非1数字退出)")
    print("==========================================")
    title = input("请选择：")
    if title=='1':
        num1 = input("请输入第一个数字：")
        fh = input('请输入+-*/%//符号中的一个：')
        num2 = input("请输入第二个数字：")
        sum = 0
        if fh=="+":
            sum = float(num1) + float(num2)
        elif fh=="-":
            sum = float(num1) - float(num2)
        elif fh=="*":
            sum = float(num1) * float(num2)
        elif fh=="/":
            sum = float(num1) / float(num2)
        elif fh=="%":
            sum = float(num1) % float(num2)
        elif fh=="//":
            sum = float(num1) // float(num2)
        if fh in list_fh:
            print("运算结果为：" + num1 + fh + num2 + "=" + str(sum))
        else:
            print('对不起，您输入的符号不存在，不能帮您计算！')
        print("=====================================")
    else:
        print('正在退出当前系统中..............')
        break

