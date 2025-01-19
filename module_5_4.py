class House:
    houses_history = []

    def __new__(cls, *args):
        return super().__new__(cls)

    def __init__(self, *args):
        self.args = args
        House.houses_history.append(self.args[0])

    def __del__(self):
        print(f"{self.args[0]} снесён, но он останется в истории")



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
# Удаление объектов
del h2
del h3
print(House.houses_history)
