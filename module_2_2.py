first  = int(input("Введите первое число:"))
print('Первое число: ', first)
second = int(input("Введите второе число:"))
print('Второе число: ', second)
third  = int(input("Введите третье число:"))
print('Третье число: ', third)

if first == second == third:
    print('Все введенные числа равны, результат: 3')
elif(first == second) or (second ==third) or (first == third):
    print('Равны 2 из 3 введенных чисел, результат: 2')
else:
    print('Среди введенных чисел нет одинаковых, результат: 0')