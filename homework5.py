tuple_immutable_var = "d", "i", 2, 1
print(tuple_immutable_var)

#tuple_immutable_var[0] = 18
#print(tuple_immutable_var)  ------> Выдает ошибку, потому что кортеж является неизменяемым типом данных
# и не поддерживает обращения по элементам

mutable_list = [2, 1, 'd', 'i', 'lists']
mutable_list[4] = 'Modified'
print(mutable_list)