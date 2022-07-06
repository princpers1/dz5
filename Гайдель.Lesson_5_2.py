import random
i = int(random.randint(1,10))
d = int(random.randint(1,2))
n=0
print(i,d)
while n < 5:
    n+=1
    c = int(input('Введите число:'))
    v = int(input('Введите цвет:'))
    if c > i:
        print('Введите число меньше!')
        if v ==d:
            print('Вы угодали цвет!')
        else:
            print('Вы не угадали цвет!')
    elif c < i:
        print('Введите число больше!')
        if v ==d:
            print('Вы угодали цвет!')
        else:
            print('Вы не угадали цвет!')
    elif c == i and v != d:
        print('Вы угадали число но не угадали цвет')
    elif c == i and v == d:
        print("Поздравляю",i,d)
        break
    if i <5:
        print('Попробуйте снова!')
    else:
        print('Вы проиграли!Правильная комбинация:',i,d)
        break




