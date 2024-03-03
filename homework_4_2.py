x = int(input('Введите число: '))
total = 0
for i in range(1, x + 1):
    if x % i == 0:
        total += 1
print('У числа', total, 'делителей.')