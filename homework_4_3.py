total = 0
even = []
for i in range(int(input('Введите первое число: ')), int(input('Введите второе число, больше первого: ')) + 1):
    if i % 2 == 0:
        total += 1
        even.append(i)
print('На заданном отрезке', total, 'четных чисел.')
print('Вот эти числа:', *even)
