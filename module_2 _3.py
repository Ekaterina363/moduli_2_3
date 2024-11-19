my_list = [ 42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5 ]
print(type(my_list))
while 1 > 0:
    number = int(input("Введите число   "))
    if number > 0:
        print("Положительное число")
    elif number == 0:
        print("Число 0")
    elif number < 0:
        print("Отрицательное число")
        break
print("Выход за границу") 



