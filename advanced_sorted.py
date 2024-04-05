def rec_binary(n):
    if n < 2:
        return str(n)
    else:
        return rec_binary(n // 2) + str(n % 2)


def mulltiplication(n, q):
    if q == 0:
        return 0
    else:
        return n + mulltiplication(n, q - 1)


def mulltiplication2(n, q):
    if q == 0:
        return 1
    elif q == 1:
        return n
    else:
        return mulltiplication2(n, q - 1) * n


n = 13
q = 4
print(f'Двоичное представление числа {n}: {rec_binary(n)}')
print(f'Число {n} умноженное на {q} равняется {mulltiplication(n, q)}')
print(f'Число {n} в степени {q} равно {mulltiplication2(n, q)}')
