def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_all(n):
    l = []
    res = factorial(n)
    for i in range(res, 0, -1):
        fact = 1
        for j in range(1, i + 1):
            fact *= j
        l.append(fact)
    return l

print(factorial_all(int(input('Введите число: '))))
