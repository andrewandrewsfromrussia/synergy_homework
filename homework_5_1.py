n = int(input('Введите количество чисел: '))
a = []
for _ in range(n):
    a.append(int(input('Введите число: ')))
for i in range(len(a) -1, -1, -1):
    print(a[i])