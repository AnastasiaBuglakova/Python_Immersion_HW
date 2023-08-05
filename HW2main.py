# 1 Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое
# представление. Функцию hex используйте для проверки своего результата.
from math import gcd

# inputed_number = int(input("Введите целое число: "))
# check = inputed_number
# print(inputed_number)
# res = ''
# st = '0123456789abcdef'
#
# while inputed_number > 0:
#     res = st[inputed_number % 16] + res
#     inputed_number //= 16

# print(res)
# print('0x'+res == hex(check))

# 2 Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

import fractions

n1, n2 = input('Введте первое дробное число через /: '), input('Введте второе дробное число через /: ')

mult = 1
n1_1, n1_2 = int(n1.split('/')[0]), int(n1.split('/')[1])
n2_1, n2_2 = int(n2.split('/')[0]), int(n2.split('/')[1])

common_del_summ = gcd(n1_1 * n2_2 + n2_1 * n1_2, n1_2 * n2_2)
summ = str(int((n1_1 * n2_2 + n2_1 * n1_2) / common_del_summ)) + '/' + str(int((n1_2 * n2_2) / common_del_summ))

common_del_mult = common_del_summ = gcd(n1_1 * n2_1, n1_2 * n2_2)
mult = str(int(n1_1 * n2_1/common_del_mult)) + '/' + str(int(n1_2 * n2_2 / common_del_mult))
print(summ, mult)

summ_check = fractions.Fraction(n1_1, n1_2) + fractions.Fraction(n2_1, n2_2)
mult_check = fractions.Fraction(n1_1, n1_2) * fractions.Fraction(n2_1, n2_2)
print(summ_check, mult_check)