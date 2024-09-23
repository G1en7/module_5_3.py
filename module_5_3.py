class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self. number_of_floors = number_of_floors


    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('такого этажа не существует')
        else:
            for floor in range(new_floor):
                print(floor + 1)

    def __str__(self):
        hom = str(f'Название:{self.name}, кол-во этажей:{self.number_of_floors}')
        return hom

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self

    def __iadd__(self, value):
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        self.number_of_floors = value + self.number_of_floors
        return  self



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2)
h1 = h1 + 10
print(h1)
print(h1 == h2)
h1 += 10
print(h1)
h2 = 10 + h2
print(h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)
