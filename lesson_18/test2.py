"""
语法：
    try:
        <尝试捕获异常>
    except Exception[as reason]:
        <异常处理>
"""
try:
    print(1/0)
except ZeroDivisionError as e: #这个异常类可以写，也可以不写；
    print(e.__doc__)
    print('除数不能为0')

