#                    Задание 3
# Найдите наименьший четный элемент списка.
# Если такого нет, то выведите первый элемент.
# Преобразовать список так, чтобы сначала шли нулевые элементы, а затем все остальные.


print("Задание №3\n")
amount_of_elements = int(input("Введите количество элементов спиcка: "))
quantity = 0
list_of_numbers = []
while quantity != amount_of_elements:
    quantity += 1
    in_element = int(input("Элемент {} : ".format(quantity)))
    list_of_numbers.append(in_element)
print("Ваш список: ", list_of_numbers)
new_list = []
for element in list_of_numbers:
    next_element = element
    if next_element % 2 == 0 and next_element != 0:
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
    print("First = ", list_of_numbers[0])
for index in range(len(list_of_numbers)):
    if list_of_numbers[index] == 0:
        list_of_numbers.pop(index)
        list_of_numbers.insert(0, 0)
print("Новый список: ", list_of_numbers)
