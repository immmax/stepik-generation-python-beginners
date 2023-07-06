#-----------------------------------------------#
# DATE: 2023.07.06                              #
# AUTHOR: Maxim Datskiy                         #
# GitHub: https://github.com/immmax             #
#-----------------------------------------------#
# Курс "Поколение Python": Курс для начинающих  #
#                                               #
# Модуль 15 - Работа над мини-проектом          #
# Урок 15.4 - Генератор безопасных паролей      #
# Шаг 1-6                                       #
#-----------------------------------------------#

import random

digits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
unclear = 'il1Lo0O'
chars = ''

number_of_passwords  = int(input('Количество паролей для генерации: '))
password_length      = int(input('Длину одного пароля: '))
digits_included      = input('Включать ли цифры 0123456789? д - да, н - нет: ').lower() == 'д'
uppercase_included   = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? д - да, н - нет: ').lower() == 'д'
lowercase_included   = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? д - да, н - нет: ').lower() == 'д'
punctuation_included = input('Включать ли символы !#$%&*+-=?@^_? д - да, н - нет: ').lower() == 'д'
unclear_excluded     = input('Исключать ли неоднозначные символы il1Lo0O? д - да, н - нет: ').lower() == 'д'

if digits_included:         chars += digits
if uppercase_included:      chars += uppercase_letters
if lowercase_included:      chars += lowercase_letters
if punctuation_included:    chars += punctuation
if not unclear_excluded:    chars += unclear

def generate_password(length: int, chars: str):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password

print('Сгенерированные пароли:')
for _ in range(1, number_of_passwords +1):
    print(str(_) + '. ' + generate_password(password_length, chars))