first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = \
    ( (len(item[0]) - len(item[1]))
      for item in zip(first, second)
      if (len(item[0]) - len(item[1])) != 0 )

second_result = \
    ( len(first[i]) == len(second[i]) for i in range(0, len(first)) )

print(list(first_result))
print(list(second_result))