  # Создаю два списка с любым количеством значений, через пробел:
l1 = map(int, input('Введите первый список чисел через пробел: ').split())
l2 = map(int, input('Введите второй список чисел через пробел: ').split())

  # Создаю множество:
s = set()

  # Добавляю значения из списка 1 в множество s:
for i in l1:
    if i not in s:
        s.add(i)

  # Добавляю значения из списка 2 в множество s:
for i in l2:
    if i not in s:
        s.add(i)

  # Вывожу результат:
print(len(s))