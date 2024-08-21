grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = list(students)
students.sort()

# Т.к. циклы мы пока не изучали, обращаемся к элементам списков напрямую.

# Первый вариант
resulting_dict_1 = dict([[students[0], sum(grades[0])/len(grades[0])],[students[1], sum(grades[1])/len(grades[1])],
                       [students[2], sum(grades[2])/len(grades[2])],[students[3], sum(grades[3])/len(grades[3])],
                       [students[4], sum(grades[4])/len(grades[4])]])
print(resulting_dict_1)

# Второй вариант
grades_mod = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]),
          sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]

resulting_dict_2 = dict(zip(students, grades_mod))
print(resulting_dict_2)