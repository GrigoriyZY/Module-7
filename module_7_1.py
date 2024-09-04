# Задача "Учёт товаров"

class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):                          # Переопределение метода __str__.
        return f'{self.name}, {self.weight}, {self.category}\n'


class Shop:
    __file_name = 'products.txt'                # Файл, в котором хранится список продуктов.

    def __init__(self):
        pass

    def get_products(self):                     # Метод для получения списка продуктов в магазине.
        file = open(self.__file_name, 'r')
        products_list = file.read()
        file.close()
        return products_list

    def add(self, *products):                   # Метод добавления продуктов в магазин
        """
        Метод получает в качестве аргумента несколько объектов класса Products.
        Выполняется проверка на наличие данных продуктов по наименованию в файле products.txt.
        Если продукт с таким названием найден, то выводится сообщение оь этом.
        В противном случае, новый продукт добавляется в файл.
        """

        for i in range(len(products)):
            if products[i].name in self.get_products():
                print(f'Продукт {products[i].name} уже есть в магазине.')
            else:
                file = open(self.__file_name, 'a')
                file.write(products[i])
                file.close()


# Код для проверки работы

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Apple', 5.5, 'Fruit')

print(p2)                                       # Проверка переопределенного метода __str__.

s1.add(p1, p2, p3)                     # Добавление продуктов в магазин.

print(s1.get_products())                        # Получение списка продуктов в магазине.
