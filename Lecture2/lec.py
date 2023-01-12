# Как работать с файлами:
# Связать файловую переменную с файлом,
# определив модификатор работы
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных
# w+, r+


# 1. Способо записи данных 

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # Разделителей не будет
# # data.writelines(colors)
# data.write('LINE 2\n')
# data.write('LINE 3\n')
# data.close()

# 2. Способ записи даннных

# with open('file2.txt', 'a') as data:
#     data.write('LINE 2\n')
#     data.write('LINE 3\n')


# Чтение данных

# path = 'file.txt'
# data = open(path, 'r')
# for i in data:
#     print(i)
# data.close()    

# exit()



# Импорт функции из другого файла по имени файла


# import hello as h


# print(h.f(10))

# print(h.new_string(5, 10))

# print(h.concatenatio('d', 'b', 'c', 'd'))
# print(h.concatenatio('4', '5', 'c', '7'))



# my_list = []

# for n in range(1, 10):
#     my_list.append(h.fib(n))
# print(my_list)    



#  Работа со словорями



# my_dictionary = {}  # Пустой словарь
# my_dictionary = \
#     {
#         'up' : 'Вверх',
#         'left' : 'Влево',
#         'right': 'Вправо',
#         'down' : 'Вниз'
#     }

# print(my_dictionary)
# print(my_dictionary['left'])





# Множества


a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q = a \
    .union(b) \
    .difference(a.intersection(b))

# {1, 21, 3, 13}

