# В файле хранятся числа, нужно выбрать чётные и составить список пар (число; квадрат числа)

# Пример 
# 1 2 3 5 8 15 23 38

# Получить:
# [(2, 4), (8, 64), (38, 1444)]

with open('lec3.txt', 'w') as data:
    data.write('1 2 3 5 8 15 23 38')

f = open('lec3.txt', 'r')
data = f.read()
f.close

data = list(map(int, data.split()))
print(data)
data = list(filter(lambda x: not x % 2, data))
print(data)
data = list(map(lambda x: (x, x ** 2), data))
print(*data)

# res = []

# for i in range(0, len(data1)):
#     if data1[i] % 2 == 0:
#         res.append((data1[i], data1[i] ** 2))
        

# print(res)        