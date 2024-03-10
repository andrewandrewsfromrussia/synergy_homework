n = int(input('Кол-во: '))
l = map(int, input('Значения через пробел: ').split())
s = set()
t = 0

for i in l:
    if i not in s:
        s.add(i)
    else:
        t += 1

print('Уникальных значений: ', len(s))
print('Повторяются: ', t)