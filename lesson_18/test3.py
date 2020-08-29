"""
语法：多挂异常
    try:
        <尝试捕获异常>
    except Exception[as reason]:
        <异常处理1>
    except Exception[as reason]:
        <异常处理2>
简写：
    try:
        <尝试捕获异常>
    except(Exception1,Exception2...)[as reason]:
        <异常处理>

"""
try:
    str = '1' + 1
    num = 1 / 0
    print(num)
    print(str)
except ZeroDivisionError as e1:
    print('异常出错原因：'+str(e1))
except TypeError as e2:
    print("异常出错原因2："+str(e2))
#由于代码的执行顺序是从上往下，所以先遇到的异常就直接跳到except代码块；
try:
    str = '1' + 1
    num = 1 / 0
    print(num)
    print(str)
except(ZeroDivisionError,TypeError) as e:
    print("异常出错原因：" + str(e))
