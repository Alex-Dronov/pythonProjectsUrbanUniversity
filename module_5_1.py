class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

        print(f'Дом \"{self.name}\", количество этажей: {self.number_of_floors}')

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print()
            print(f'Этажа № {new_floor} в доме с названием \"{self.name}\" не существует')
        else:
            print()
            for i in range(1, new_floor + 1):
                print(i)
            print('Всё, приехали.')

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)