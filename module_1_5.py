immutable_var = (1, "строка", 3.14, True, [1, 2, 3])
print(immutable_var)
try: immutable_var[0] =10
except TypeError as e:
 print("Ошибка:", e)
print("Нельзя изменить значения элементов кортежа, так как кортежи являются неизменяемыми (immutable) объектами в Python.")

mutable_list = [1, 2, 3, "четыре", 5.0]
print("Изначальный список:", mutable_list)
mutable_list[0] = 10
mutable_list[3] = "новая строка"
print("Измененный список:", mutable_list)