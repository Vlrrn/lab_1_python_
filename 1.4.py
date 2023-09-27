#                    Задание 4
# Создайте словарь из строки 'Follow your heart' следующим образом:
# в качестве ключей возьмите символы строки, а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку


print("Задание №4\n")
string = "Follow your heart"
print(string)
dictionary = {}                                 # создание пустого словаря
for el in string:                               # перебор символов строки
    # print(el, ', ', dictionary.get(el))       # текущий символ, значение для ключа-символа в словаре
    dictionary[el] = dictionary.get(el, 0) + 1  # возвращается значение по указанному ключу (default 0), + 1
                                                # и устанавливается в качестве значения соответствующего ключа
    # print(el, ', ', dictionary[el])           # символ, обращение к значению по ключу
print(', '.join(([str(i) for i in dictionary.items()])))
for key, value in dictionary.items():
    print(key, ' - ', value)
for el in dictionary:
    print(el, ' - ', dictionary[el])
print(dictionary.items())
print(dictionary.keys())
print(dictionary.values())

#------------------------------------
# for key in dictionary:
#     print(key)
# for key in dictionary.keys():
#     print(key)
# for value in dictionary.values():
#     print(value)
# for pair in dictionary.items():
#     print(pair)
# for key, value in dictionary.items():
#     print(key, ": ", value)
#-------------------------------------