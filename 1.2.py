#                    Задание 2.
# Дана строка, в которой имеется текст в скобках.
# Удалить часть текста, заключенного в скобки


print("Задание №2\n")
text = input("Введите строку с текстом в скобках: ")
start_index = text.find("(")
end_index = text.find(")")
# print("Ваш текст: {}\nИндекс ( = {}\nИндекс ) = {}\n".format(text, start_index, end_index))
while start_index != -1 and end_index != -1:
    text = text[:start_index] + text[end_index + 1:]
    start_index = text.find("(")
    end_index = text.find(")")
    # print("Часть удалена!\nТекст: {}\nИндекс ( = {}\nИндекс )= {}\n".format(text, start_index, end_index))
new_text = text
print("Новый текст: ", new_text)

