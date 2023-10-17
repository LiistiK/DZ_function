class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    # Задание 1
    def pr(self):
        return f"Название автомобиля: {self.name}. Скорость: {self.max_speed}. Пробег: {self.mileage}"

    # Задание 2
    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"


Autobus = Transport('Renault Logan', 180, 12)

#Вывод для задание 1
print(Autobus.pr())

#Вывод для задания 2
print(Autobus.seating_capacity(50))


