import os
path = os.getcwd()
file_name = 'recipes.txt'
full_path = os.path.join(path, file_name)
cook_book = {}
list = []
slovar_2 = {}
class Slovar:
    def __init__(self, ingridient_name, quantity, measure):
        self.ingridient_name = ingridient_name
        self.quantity = quantity
        self.measure = measure
        self.slovar = {}
    def add_slovar(self):
        self.slovar['ingridient_name'] = self.ingridient_name
        self.slovar['quantity'] = self.quantity
        self.slovar['measure'] = self.measure
        list.append(self.slovar)
        print(self.slovar)

with open(full_path, 'r', encoding='utf-8') as file:
    def read_recipe():
        dish_name = file.readline()
        number = int(file.readline())
        i = 0
        while i < number:
            count = 0
            ingridient_name = ''
            quantity = ''
            measure = ''
            i += 1
            string = file.readline()
            for symbol in string:
                if symbol != '|':
                    if symbol != ' ':
                        if count == 0:
                            ingridient_name += symbol
                        if count == 1:
                            quantity += symbol
                        if count == 2:
                            measure += symbol
                else:
                    count += 1
            slovar = Slovar(ingridient_name, quantity, measure)
            slovar.add_slovar()
        slovar_2[dish_name] = list
    read_recipe()
print(slovar_2)
