class Transport:
   def __init__(self, name, max_speed, mileage):
       self.name = name
       self.max_speed = max_speed
       self.mileage = mileage

   def seating_capacity(self, capacity):
       return f"Вместимость одного автобуса {self.name} - {capacity} пассажиров"

   def info(self):
       return f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}"

autobus = Transport("PAZik", 80, 788000)
print(autobus.info())
print(autobus.seating_capacity(50))



