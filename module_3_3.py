def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(b = 25)      # работает, результат: 1 25 True
print_params(c = [1,2,3]) # работает, результат: 1 строка [1, 2, 3]
print()

values_list = ['Подстрока', False, 777]
#values_dict = {'b': 1000, 'c': 'SubString', 'a': 'TrueOrFalse'}
values_dict = dict(b = 1000, c = 'SubString', a = 'TrueOrFalse')
print_params( *values_list )
print_params( **values_dict )
print()

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 45)