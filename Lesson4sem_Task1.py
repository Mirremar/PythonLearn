#Задача:Вывести через '_' количество раз,которое символ уже встречался ранее

def counter(array):
    splarray = array.split()
    alreadymet = dict()
    res = ''
    for i in range(len(splarray)):
        if splarray[i] not in alreadymet:
            alreadymet[splarray[i]] = 1
            res += splarray[i] + ' '
        else:
            res+=str(splarray[i])+'_'+str(alreadymet[splarray[i]]) + ' '
            alreadymet[splarray[i]] += 1
    return res
somestr = input("enter string")
print(counter(somestr))