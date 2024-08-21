immutable_var = ( "Первый", 2, "третий", True, "Ложь", False, 7)
print(type(immutable_var))
print(immutable_var)
print()

# Попытка изменить кортеж (см. следующий оператор в комментарии) вызовет ошибку,
# т.к. кортеж относится к неизменяемым объектам
# immutable_var[3] = False

mutable_list = [ "Первый", 2, "третий", True, "Ложь", False, 7]
print(type(mutable_list))
print(mutable_list)
print()

mutable_list[3] = False
mutable_list[0] = 1
mutable_list[6] = "seven"
print("Измененный список mutable_list:")
print(mutable_list)