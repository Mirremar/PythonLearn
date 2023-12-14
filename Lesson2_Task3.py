number=[]
i=0
amount = int(input("Enter amount of numbers"))
for i in range(0,amount):
    number.append(int(input(f'enter an {i+1} Element')))
print(f'Mininmum is {min(number)}')
print(f'maximum is {max(number)}')
