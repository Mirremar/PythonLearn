l = []
x,y = 3,3
for i in range(1,y+1):
    temp = []
    for j in range(1,y+1):
        temp.append(i*j)
    l.append(temp)

for i in l:
    for j in i:
        print(j,end=' ')
    print()
