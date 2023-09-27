#                    Задание 1.
# Найти максимальную цифру введенного натурального числа.


print("Задание №1\n")
number = int(input("Введите натуральное число: "))
max_digit = 0
while number > 0:
    digit = number % 10
    if digit > max_digit:
        max_digit = digit
    number = number // 10
print("Максимальная цифра в числе:", max_digit)
