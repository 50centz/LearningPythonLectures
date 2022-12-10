# print('Hello world')


# Типы данных справедливы
# int, float, boolean, str, list, None

# value = None
# print(type(value))
# a = 123
# b = 1.23

# print(type(a))
# print(type(b))
# value = 123456
# print(type(value))

# s = '"Hello, world"'
# print(a, '-',  b,  '-', s) # Вывод строки
# print('{} - {} - {}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = False
# print(f)


#   Array(Массив)

# list = ['1', '2', ' hello world']
# col = [1, 2, 3.5]
# print(list)
# print(col)





# print("Input a: ")
# a = int(input())
# print("Input b: ")
# b = int(input())


# print("Input a: ")
# a = float(input())
# print("Input b: ")
# b = float(input())

# print(a, '+', b, ' = ', a + b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')







#    Арифметические операции

#    +, -,*, /, %, //,**
#    Приоритет операций
#    **, ⊕, ⊖,*, /, //, %, +, -
#    ( ) Скобки меняют приоритет


# a = 2.54514645
# b = 800
# c = round(a * b, 3)
# print(c)





#    Логические операции

#    >, >=, <, <=, ==, !=
#    not, and, or – не путать с &, |,^
#    Кое-что ещё: is, is not, in, not in


#    Управляющие конструкции: if, if-else

# username = input('Input your name: ')

# a = int(input('Input a first digit: '))
# b = int(input('Input a second digit: '))

# if a > b:
#     print(a)
# else:
#     print(b)    

# username = input('Input a name: ')
# if username == 'Mash':
#     print('Hello, Masha')
# elif username == 'Kolya':
#     print('Hello, Kolya')
# elif username == 'Vasya':
#     print('Hello, Vasya')
# else:
#     print('Hello, ', username)    





#    Управляющие конструкции: while


# original = 43
# inverted = 0

# while original != 0:
#     inverted = inverted * 10 + (original %10)
#     original //= 10
# print(inverted)    





# original = 43
# inverted = 0

# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     print(inverted)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй,')
#     print('хватит')    
# print(inverted)  





#    Управляющие конструкции: for


# list = [1, 2, 3, 4, 10, 5]
# for i in 1, 2, 3, 4, 5:
#     print(i ** 2)


# for i in list:
#     print(i ** 2)


# r = range(11)
# for i in r:
#     print(i)



# for i in range(6):
#     print(i)


# for i in range(1, 10, 3):
#     print(i)


# for i in 'qwerty':
#     print(i)



# line = ""
# for i in range(5):
#  line = ""
#  for j in range(5):
#      line += "*"
#  print(line)





#    Немного о строках



# text = 'съешь ещё этих мягких французских булок'

# #    help(text.isdigit)


# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#  print(c)





# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...






# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#  i *= 2
#  print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]




# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент






#    Функции



# def function_name(x):
    # body line 1
    # . . .
    # body line n
    # optional return


# x = 4

# def f(x):
#     return x ** 2

# print(f(x)) 


def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return x    

a = 2.3
print(f(a))