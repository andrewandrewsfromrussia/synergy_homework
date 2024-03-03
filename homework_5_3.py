n = int(input('Введите кол-во рыбаков: '))
m = int(input('Введите грузоподьемность лодки: '))
people = [int(input('Введите вес рыбака:')) for _ in range(n)]
print(people)

result = []

while len(people) > 1:
    a = []
    x = max(people)
    people.remove(max(people))
    for j in range(len(people)):
        y = x + people[j]
        if y <= 150:
            a.append(y)
    if a == []:
        result.append(x)
    else:
        result.append(max(a))
        people.remove(max(a) - x)


print('Необходимо лодок:', len(result))








