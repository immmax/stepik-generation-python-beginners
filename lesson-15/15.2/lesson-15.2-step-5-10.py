#-----------------------------------------------#
# DATE: 2023.06.20                              #
# AUTHOR: Maxim Datskiy                         #
# GitHub: https://github.com/immmax             #
#-----------------------------------------------#
# Курс "Поколение Python": Курс для начинающих  #
#                                               #
# Модуль 15 - Работа над мини-проектом          #
# Урок 15.2 - Числовая угадайка                 #
# Шаг 5-10                                      #
#-----------------------------------------------#

from random import randint

print("Добро пожаловать в числовую угадайку")

def get_right_limit():
    return int(input(f"Я загадаю число от {left_limit} до (введите максимальное число): "))

def is_valid(number):
    return number.isdigit() and (left_limit <= int(number) <= right_limit)

left_limit = 1
right_limit = get_right_limit()
n = randint(left_limit, right_limit)
count = 0

while True:
    user_number = input(f">>> Попробуй угадать число от {left_limit} до {right_limit}: ")
    count += 1
    if is_valid(user_number):
        user_number = int(user_number)
    else:
        print(f'А может быть всё-таки введем целое число от {left_limit} до {right_limit}?')
        continue

    if user_number == n:
        print(f"Вы угадали число {n} за {count} ходов! Поздравляем!")
        if input("Хотите сыграть ещё? да/нет: ").lower() == 'да':
            count = 0
            right_limit = get_right_limit()
            n = randint(left_limit, right_limit)
        else:
            break
    else:
        if user_number < n:
            quality = "больше"
        elif user_number > n:
            quality = "меньше"
        print(f'Ваше число {quality} загаданного, попробуйте еще разок')
     
print('Спасибо, что играли в числовую угадайку. Ещё увидимся...')