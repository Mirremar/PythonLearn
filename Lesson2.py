import math
#print(math.factorial(int(input("Enter a number to factorial"))))

fibs = [0,1]
curFibNum = 0
num = int(input("Enter a presumably fibbonacci number"))
i=2
flag = bool(False)
if num == 0:
    print("this is a 1st fibonacci number")
elif num == 1:
    print("this is a 2nd fibonacci number")
else:
    while curFibNum <= num:
        curFibNum = (fibs[i - 1] + fibs[i - 2])
        if curFibNum == num:
            print("This is a " + str(i+1) + " fibonacci number")
            flag = bool(True)
            break
        else:
            fibs.append(curFibNum)
            i+=1
if flag == bool(False):
    print("it is not a fibonacci number")

