def custom_write(file_name, strings):
    strings_positions = {}
    string_num = 0
    new_file = open(file_name, 'w', encoding='utf-8')

    for str_ in strings:
        string_num += 1
        strings_positions.__setitem__((string_num, new_file.tell()), str_)
        new_file.write(str_ + '\n')

    new_file.close()

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
