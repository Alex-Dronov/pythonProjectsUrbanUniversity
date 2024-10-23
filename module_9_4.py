# Метод __call__:

from random import choice

class MysticBall:

    def __init__(self, *words ):
        self.words = words

    def __call__(self, *args, **kwargs):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print()


# Замыкание:

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        my_file = open(file_name, 'a')
        for str_ in data_set:
            my_file.write(str(str_) + '\n')
        my_file.close()

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
with open('example.txt') as file_:
    for line_ in file_:
        print(line_, end = '')
print()


# Lambda-функция:

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))