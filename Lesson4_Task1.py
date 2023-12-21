#В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
#(число; квадрат числа).
#Пример: 1 2 3 5 8 15 23 38
#Получить: [(2, 4), (8, 64), (38, 1444)]


array = [1, 2, 3, 5, 8, 15, 23, 38]
#res = list()
#for i in array:
#    if i%2==0:
#        res.append((i,i**2))
#print(res)

def select(f,col):
    return [f(x) for x in col]  #список из элементов,к которым применили функцию f(x)
def where(f,col):
    return [x for x in col if f(x)] #список из элементов,для которых выполняется условие true
res = select(int,array) #преобразовали всё в int
res = where(lambda x:x%2==0,res) #выбрали чётные
print(res)
res = list(select(lambda x: (x,x**2),res)) #возвели в квадрат
print(res)