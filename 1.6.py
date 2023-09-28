#                           Задание 6
# Даны два кортежа.
# Создайте третий кортеж, который будет включать в себя элементы первого и второго.


print("Задание №6\n")
first_tuple_ = (1, 4, 7, 2, "end")
second_tuple_ = (0, 'one', [1, "List", 3 + 2j], 2.2)
third_tuple_ = first_tuple_ + second_tuple_
print("1 кортеж: ", first_tuple_, "\n2 кортеж: ", second_tuple_, "\n")
print("Новый кортеж: ", ', '.join([str(i) for i in third_tuple_]))