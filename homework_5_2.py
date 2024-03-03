n = int(input('Введите кол-во чисел: '))
list = list(map(int, input('Введите числа через пробел: ').split()))
re_list = []
for i in range(0, n):
    re_list.append(list[i - 1])
print(*re_list)
