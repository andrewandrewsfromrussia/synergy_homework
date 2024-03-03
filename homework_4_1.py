n = int(input('Введите кол-во целых чисел: '))
total = 0
for i in range(n):
    if int(input('Введите целое число: ')) == 0:
        total += 1
print('Нулю равно', total, 'целых чисел.')
