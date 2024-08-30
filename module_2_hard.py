inp_ = 0
while True:
    inp_ = int(input("Введите целое число от 3 до 20:"))

    if inp_ < 3 or inp_ > 20:
        print("Вы ввели неправильное число")
    else:
        print("Вы ввели цифру:", inp_)
        break

result = ''
for i in range( 1, 20):
    for j in range( i+1, 20):
        if inp_ % (i + j) == 0:
            result += str(i) + str(j)

print(result)