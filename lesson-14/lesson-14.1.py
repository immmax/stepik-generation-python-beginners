#-----------------------------------------------#
# DATE: 2023.07.11                              #
# AUTHOR: Maxim Datskiy                         #
# GitHub: https://github.com/immmax             #
#-----------------------------------------------#
# Курс "Поколение Python": Курс для начинающих  #
#                                               #
# Модуль 14 - Итоговая работа по функциям       #
# Урок 14.1                                     #
#                                               #
#-----------------------------------------------#

def draw_triangle():
    for i in range(1, 9):
        for j in range(0, 7+i):
            if j < 8-i:
                print('_', end='')
            else:
                print('*', end='')
        print()

draw_triangle()