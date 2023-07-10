#-----------------------------------------------#
# DATE: 2023.07.07                              #
# AUTHOR: Maxim Datskiy                         #
# GitHub: https://github.com/immmax             #
#-----------------------------------------------#
# Курс "Поколение Python": Курс для начинающих  #
#                                               #
# Модуль 15 - Работа над мини-проектом          #
# Урок 15.5 - Шифр Цезаря                       #
# Шаг 1-10                                      #
#-----------------------------------------------#
'''
alphabets = [32, 26]
limits = {'lower': {0: ['я', 'z'], 1: ['а', 'a']},
          'upper': {0: ['Я', 'Z'], 1: ['', 'A']}}

def get_limit(char, direction, language):
    if char.isupper():      limit = ord(limits['upper'][direction][language])
    elif char.islower():    limit = ord(limits['lower'][direction][language])
    return limit

try:
    direction = int(input("Направление: 0 - шифрование, 1 - дешифрование: "))
    language = int(input("Язык шифрования: 0 - русский, 1 - английский: "))
    shift_step = int(input("Шаг сдвига: "))
except:
    print("Неверные данные. Программа прервана.")
    exit()

if direction == 1:
    shift_step = - shift_step

initial_phrase = input('Исходная фраза: ')
result_phrase = ''

def get_new_char(char):
    new_char = ord(char)
    if char.isalpha():
        current_shift_step = shift_step
        limit = get_limit(char, direction, language)
        if direction == 1:
            if ord(char) + shift_step < limit:
                current_shift_step = shift_step + alphabets[language]
        else: 
            if ord(char) + shift_step > limit:
                current_shift_step = shift_step - alphabets[language]
        new_char = ord(char) + current_shift_step
    return new_char

for char in initial_phrase:
    new_char = get_new_char(char)
    print(f'{char} ---> {ord(char)} -> {new_char} ---> {chr(new_char)}')

    result_phrase += chr(new_char)

print(f'Конечная фраза: {result_phrase}') '''

#-----------------------------------------------#
# Урок 15.5 - Шифр Цезаря                       #
# Шаг 10                                        #
#-----------------------------------------------#
alphabet = 26
limits = {'lower': 'z', 'upper': 'Z'}

string_to_code = input("Введите строку для шифрования: ").split()
print(string_to_code)
result_string = ''

def get_limit(char):
    if char.isupper():      limit = ord(limits['upper'])
    elif char.islower():    limit = ord(limits['lower'])
    return limit

def get_new_char(char, shift_step):
    new_char = ord(char)
    if char.isalpha():
        current_shift_step = shift_step
        limit = get_limit(char)
        if ord(char) + shift_step > limit:
            current_shift_step = shift_step - alphabet
        new_char = ord(char) + current_shift_step
    return new_char

for word in string_to_code:
    shift_step = 0
    for char in word:
        if char.isalpha():
            shift_step += 1
    for char in word:
        if char.isalpha:
            result_string += chr(get_new_char(char, shift_step))
    result_string += ' '
print(result_string)