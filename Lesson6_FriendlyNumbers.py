#Задача поиска дружественных чисел

k = int(input("Enter k"))

numbers = [0]*(k+1)
numbers[1]=1
temp=0
for i in range(2, len(numbers)):
    for j in range(1,i+1):
        if (i%j==0):
            temp+=j
    temp -= i
    numbers[i] = temp
    temp=0
print(numbers)

for i in range(1,len(numbers)):
    for j in range(2,len(numbers)):
        if (numbers[i] == j) and (numbers[j]==i) and (i<j):
            print(f'{i,j}')