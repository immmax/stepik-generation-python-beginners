#-----------------------------------------------#
# DATE: 2023.07.09                              #
# AUTHOR: Maxim Datskiy                         #
# GitHub: https://github.com/immmax             #
#-----------------------------------------------#
# Курс "Поколение Python": Курс для начинающих  #
#                                               #
# Модуль 15 - Работа над мини-проектом          #
# Урок 15.6 - Калькулятор систем счисления      #
# Шаг 1-10                                      #
#-----------------------------------------------#

# "Ручной" перевод числа из двоичной системы в десятичную
# number = '111111'
# result = 0
# for digit in range(len(number)-1, -1, -1):
#     result += 2 ** digit
# print(result)

# То же самое, но встроенными механизмами
# print(0b111111)

#-----------------------------------------------#

# Перевод из 16-ричной в 10-тичную
# print(0x1AF2)

#-----------------------------------------------#

# Задача про яблоки - определить систему счисления
# fruits = {
#     'total': 88,
#     'apple': 32,
#     'pear': 22,
#     'plum': 16,
#     'cherry': 17
# }

# system = 9

# while system < 100:
#     check = {
#         'total': 0,
#         'apple': 0,
#         'pear': 0,
#         'plum': 0,
#         'cherry': 0
#     }
#     for key, value in fruits.items():
#         result = 0
#         power = -1
#         for digit in str(value)[::-1]:
#             power += 1
#             result += int(digit) * system ** power
#         check[key] = result
#         sum = check['apple'] + check['pear'] + check['plum'] + check['cherry']
#     print(f'{system}: {check["total"]} == {sum} -> {check["total"] == sum}')
#     if check["total"] == sum:
#         break
#     system += 1

#-----------------------------------------------#

# Перевести в 16-ричную
# print(hex(1000))

#-----------------------------------------------#

# Перевести в двоичную
# print(bin(513))

#-----------------------------------------------#

# Перевод в BIN, OCT, HEX
number = int(input())

# Красивый вывод в консоли
print(f'bin\toct\thex\n{bin(number)}\t{oct(number)}\t{hex(number)}')

# Вывод для Stepik
print(bin(number)[2:])
print(oct(number)[2:])
print(hex(number)[2:].upper())