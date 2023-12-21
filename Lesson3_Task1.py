input = [2,5,1,2,5,6,7,8,9,12,456,8,3]
countslen = max(input)
counts = [0]*countslen
counts.append(0)
for i in input:
    counts[i]+=1
uniques = len(counts) - counts.count(0)
print(uniques)

###Или,можно решить так:
print(len(set(input)))