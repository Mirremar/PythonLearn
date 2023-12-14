number=[]
amount = int(input("Enter amount of numbers"))
positives=[]
count = 0
for i in range(0,amount):
    number.append(int(input(f'enter an {i+1} Element')))
    if number[i]>0:
        count+=1
    else:
        positives.append(count)
        count=0
print(f'longest pos streak is {max(positives)} positive numbers')
