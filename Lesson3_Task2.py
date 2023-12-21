#Сдвинуть элементы массива на k элементов вправо

import random
nubmers = [random.randint(-10,10) for _ in range(10)]
print(nubmers)
offset = int(input("enter offset"))
temp = 0
for _ in range(offset):
    temp = nubmers.pop()
    nubmers.insert(0,temp)
print(nubmers)
#Или можно решить так
print(nubmers[-offset:] + nubmers[:-offset])