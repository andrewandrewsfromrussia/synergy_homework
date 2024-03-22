# Создайте класс Черепашка, который хранит позиции x и y черепашки, а также s - количество клеточек, на которое она перемещается за ход
# у этого класс есть методы:
# go_up() - увеличивает y на s
# go_down() - уменьшает y на s
# go_left() - уменьшает x на s
# go_right() - увеличивает y на s
# evolve() - увеличивает s на 1
# degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
# count_moves(x2, y2) - возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции

class the_turtle(object):
    name = "Leonardo"
    x_pos = 0
    y_pos = 0
    steps = 0

    def __init__(self, name, x, y, s):
        self.name = name
        self.x_pos = x
        self.y_pos = y
        self.steps = s

    def go_up(self):
        self.y_pos += self.steps
        return f"{self.name} находится на позиции {self.x_pos} по оси Х и {self.y_pos} по оси Y."

    def go_down(self):
        self.y_pos -= self.steps
        return f"{self.name} находится на позиции {self.x_pos} по оси Х и {self.y_pos} по оси Y."

    def go_left(self):
        self.x_pos -= self.steps
        return f"{self.name} находится на позиции {self.x_pos} по оси Х и {self.y_pos} по оси Y."

    def go_right(self):
        self.x_pos += self.steps
        return f"{self.name} находится на позиции {self.x_pos} по оси Х и {self.y_pos} по оси Y."

    def evolve(self):
        self.steps += 1
        return f"{self.name} увеличил число ходов на 1."

    def degrade(self):
        if self.steps > 1:
            self.steps -= 1
            return f"{self.name} увеличил число ходов на 1."
        else:
            return f"Черепашка не может идти медленнее клетки за ход."

    def count_moves(self, x, y):
        return f"Черепашке, для осуществления перемещения в заданные координаты, необходимо {((self.x_pos >= x if self.x_pos - x else x - self.x_pos) + (self.y_pos >= y if self.y_pos - y else y - self.y_pos)) / self.steps} шагов."

turtl_1 = the_turtle("Donatello", 0, 0, 1)

print(turtl_1.go_up())
print(turtl_1.steps)
print(turtl_1.evolve())
print(turtl_1.go_up())