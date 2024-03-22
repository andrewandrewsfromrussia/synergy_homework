# Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:
# top_up(X) - пополнить на X
# count_1000() - выводит сколько целых тысяч осталось в кассе
# take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег

class cash(object):
    bank = "AO Bank"
    money = 10000

    def __init__(self, bank, money):
        self.bank = bank
        self.money = money

    def top_up(self, x):
        self.money += x
        return self.money

    def count_1000(self):
        return f"В кассе {self.money // 1000} тысяч."

    def take_away(self, x):
        if self.money - x >= 0:
            return f"Вы сняли {x} из ваших средств, остаток - {self.money - x}. Спасибо что воспользовались услугами {self.bank}"
        else:
            return f"Недостаточно средств."

x = cash("AO NEBANK", 5000)
print(x.top_up(3001))
print(x.count_1000())
print(x.take_away(3000))
