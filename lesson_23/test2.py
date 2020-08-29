"""
字典语法1：
    变量名={'key1':'value1','key2':'value2'....}
字典语法2：
    变量名=dict(key1=value1,key2=value2.....)
    key值不能加单引号或双引号；
"""
#第一种定义方式：
languages = {'P':'PHP','py':'Python','J':'Java','A':'Android'}
print(languages['py']) #输出：Python
languages['x'] = [1,2,3] #可以直接添加，也可以是列表；
print(languages) #{'P': 'PHP', 'py': 'Python', 'J': 'Java', 'A': 'Android', 'x': [1, 2, 3]}
#第二种定义方式：
languages_2 = dict(P='PHP',py='Python',J='Java',A='Android')
print(languages_2['P']) #输出：PHP
print(languages_2['PHP']) #抛出KeyError异常
