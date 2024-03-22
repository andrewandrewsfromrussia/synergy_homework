my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def funn(x):
    try:
        print(my_list[x])
        x = x + 1
        funn(x)
    except:
        print("Конец списка.")

y = 0
funn(y)