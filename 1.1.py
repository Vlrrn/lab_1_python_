#                    Задание 1.
# Найти максимальную цифру введенного натурального числа.


def check(s):
    while True:
        try:
            ii = int(input(s))
        except ValueError:
            print("Введите целое число!")
        else:
            return ii


print("Задание №1\n")
number = check("Введите натуральное число: ")
str_number = str(number)
for el in str_number:
    str_number = str_number.replace("-", '')
number = int(str_number)
print(number)
max_digit = 0
while number > 0:
    digit = number % 10
    if digit > max_digit:
        max_digit = digit
    number = number // 10
print("Максимальная цифра в числе:", max_digit)
