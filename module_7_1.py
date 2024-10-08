import os.path

class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        prod_description = self.name + ', ' + self.weight.__str__() + ', ' + self.category
        return prod_description


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        if os.path.isfile(self.__file_name): # Проверяем существует ли файл products.txt

            # Файл products.txt существует, считываем из products.txt всю информацию

            products_file = open(self.__file_name, 'r')
            products_str = products_file.read()
            products_file.close()
        else:

            # Файл products.txt не существует, создаем файл products.txt, и возвращаем пустую строку

            products_file = open(self.__file_name, 'a')
            products_file.close()
            products_str = ''

        return products_str

    def add(self, *products):

        for product_ in products:

            name_prod = product_.__str__()

            if self.get_products().find(name_prod) != -1:
                print(f'Продукт {name_prod} уже есть в магазине')
            else:
                products_file = open(self.__file_name, 'a')
                products_file.write(name_prod + '\n')
                products_file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())