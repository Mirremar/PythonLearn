#stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
phrases = stroka.split()
if len(phrases) <= 1:
    print('Количество фраз должно быть больше одной!')
    exit(0)
words=[]
vowels=['а','о','е','и','у','ы','я','ю']
counter=0
rhythmFlag=False
phrasevovelcounter=[]
for i in phrases:
    words.append(i.split('-'))
#print(words)
for phrases in words:
    for wrd in phrases:
        for i in wrd:
            if i in vowels:
                counter+=1
    phrasevovelcounter.append(counter)
    counter=0
if all(map(lambda x: x == phrasevovelcounter[0], phrasevovelcounter))==True:
    print('Парам пам-пам')
else:
    print('Пам парам')