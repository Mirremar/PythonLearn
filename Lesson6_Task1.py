#Вывести элементы,которые есть в первом массиве,но которых нет во втором

import random

list_1 = [random.randint(0,20) for i in range(20)]
print(list_1)
list_2 = [random.randint(0,20) for i in range(20)]
print(list_2)
res = list(filter(lambda x:x not in list_2,list_1))
print(res)