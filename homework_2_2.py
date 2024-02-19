num = int(input('Введите пятизначное число: '))
u = num % 10
d = (num // 10) % 10
h = (num // 100) % 10
th = (num // 1000) % 10
t_th = (num // 10000) % 10
print((d ** u) * 2 / (t_th - th))
