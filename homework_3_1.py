def exit():
    if input('Продолжить? y/n: ') == 'y':
        w_le()
    else:
        print('Всего доброго.')
        quit()

def w_le():
    try:
        num = int(input('Введите целое число: '))
    except:
        print("ОШИБКА! Пожалуйста, введите целое число.")
        w_le()
    while True:
        if num > 0 and num % 2 == 0:
            print('Введено четное положительное число')
            exit()
        elif num > 0 and num % 2 == 1:
            print('Введено нечетное положительное число')
            exit()
        elif num < 0 and num % 2 == 0:
            print('Введено четное отрицательно число')
            exit()
        elif num < 0 and num % 2 == 1:
            print('Введено нечетное отрицательно число')
            exit()
        elif num == 0:
            print('Введено нулевое число')
            exit()

w_le()






