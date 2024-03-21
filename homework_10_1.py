import random

x = int(input("Введите высоту: "))
y = int(input("Введите ширину: "))
list = [[random.randint(0, x*y) for i in range(y)] for i in range(x)]
list2 = [[random.randint(0, x*y) for i in range(y)] for i in range(x)]
list3 = list

def lst():
    for i in list:
        print(*i)
    print()
    for i in list2:
        print(*i)
    print()
    print("Сумма списков:")
    for i in range(y):
        for j in range(x):
            list3[i][j] += list2[i][j]
    for i in list3:
        print(*i)

lst()



