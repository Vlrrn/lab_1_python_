#                    Задание 3
# Найдите наименьший четный элемент списка.
# Если такого нет, то выведите первый элемент.
# Преобразовать список так, чтобы сначала шли нулевые элементы, а затем все остальные.

def check(s):
    while True:
        try:
            ii = int(input(s))
        except ValueError:
            print("Введите целое число!")
        else:
            return ii


print("Задание №3\n")
while True:
    amount_of_elements = check("Введите количество элементов спиcка: ")
    if amount_of_elements < 1:
        print("!?")
    else:
        break
quantity = 0
list_of_numbers = []
while quantity != amount_of_elements:
    quantity += 1
    in_element = check("Элемент {} : ".format(quantity))
    list_of_numbers.append(in_element)
print("Ваш список: ", list_of_numbers)
new_list = []
for element in list_of_numbers:
    next_element = element
    if next_element % 2 == 0:
        new_list.append(next_element)
if len(new_list) != 0:
    print("Чётные элементы: ", new_list)
    min = new_list[0]
    for new_element in new_list:
        new_next = new_element
        if new_next < min:
            min = new_next
    print("Min = ", min)
else:
    print("Первый = ", list_of_numbers[0])
for index in range(len(list_of_numbers)):
    if list_of_numbers[index] == 0:
        list_of_numbers.pop(index)
        list_of_numbers.insert(0, 0)
print("Новый список: ", list_of_numbers)
