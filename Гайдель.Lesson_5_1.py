list1 = [15, 48, 'hello', 6, 19 , "world"]
n = 0
v = 0
m = 0

for i in list1:
    if type(i) is int:
        if i % 2 == 0:
            i = str(i)
            for o in i:
                o = int(o)
                n += o
            print(i, 'сумма цифр:', n)
            n = 0
        else:
            ind = list1.index(i)
            list1[ind] = 1
    elif type(i) is str:
        for t in i:
            if t in 'aeoiu':
                v+=1
            else:
                 m +=1
        print(i,'Количество согластных:',m)
        print(i, 'Количество гласных:', v)
        v=0
        m=0
print(list1)