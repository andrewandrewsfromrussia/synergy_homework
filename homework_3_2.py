str = input('Введите строку данных(используйте латинские буквы и цифры: ').lower()

vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'm', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

def defination():
    vo = 0
    co = 0
    nu = 0
    for i in str:
        if i in vowels:
            vo += 1
        elif i in consonants:
            co += 1
        elif i in numbers:
            nu += 1
    print('В данной строке:')
    print('Гласных -', vo)
    print('Согласных -', co)
    print('Целых чисел -', nu)


defination()
