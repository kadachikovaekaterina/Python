# 1. Создайте программу для игры в "Крестики-нолики".

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print('{}\n{}\n{}'.format(list[:3], list[3:6], list[6:]))
# symbol1 = 'x'
# symbol2 = '0'


# def Stop_game(list):
#     terms1 = list[0] == list[1] == list[2]
#     terms2 = list[3] == list[4] == list[5]
#     terms3 = list[6] == list[7] == list[8]
#     terms4 = list[0] == list[3] == list[6]
#     terms5 = list[1] == list[4] == list[7]
#     terms6 = list[2] == list[5] == list[8]
#     terms7 = list[0] == list[4] == list[8]
#     terms8 = list[2] == list[4] == list[6]
#     list_new = [terms1, terms2, terms3, terms4, terms5, terms6, terms7, terms8]
#     return (any(list_new))


# k = 1
# while k < 9:
#     step1 = int(input('Первый игрок- играем х: введите номер ячейки '))
#     list[step1-1] = symbol1
#     print('{}\n{}\n{}'.format(list[:3], list[3:6], list[6:]))
#     k += 1
#     if k >= 4 and Stop_game(list) == True:
#         print('Победа первого игрока!')
#         break
#     step2 = int(input('Второй игрок- играем 0: введите номер ячейки '))
#     list[step2-1] = symbol2
#     print('{}\n{}\n{}'.format(list[:3], list[3:6], list[6:]))
#     k += 1
#     if k >= 4 and Stop_game(list) == True:
#         print('Победа второго игрока!')
#         break

# if k >= 9:
#     print('Ничья! Играем вновь! ')

# 2. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,. приоритет операций стандартный.
# *Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;

import re
actions = {
  "^": lambda x, y: str(float(x) ** float(y)),
  "*": lambda x, y: str(float(x) * float(y)),
  "/": lambda x, y: str(float(x) / float(y)),
  "+": lambda x, y: str(float(x) + float(y)),
  "-": lambda x, y: str(float(x) - float(y))
}
 
priority_reg_exp = r"\((.+?)\)"
action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"
 
def prim(expresion: str) -> str:
 
    while (match := re.search(priority_reg_exp, expresion)):
        expresion: str = expresion.replace(match.group(0), prim(match.group(1)))
 
    for symbol, action in actions.items():
        while (match := re.search(action_reg_exp.format(symbol), expresion)):
            expresion: str = expresion.replace(match.group(0), action(*match.groups()))
 
    return expresion
 
 
exp = "(1+2)*3 + 4*(2+6/3)"
print(exp, '=', prim(exp))

# второй вариант :)
# expression = '(1+2)*3'
# print(expression, '=', eval(expression))


# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# желательно использовать одну из функций ускоренной обработки данных где-нибудь.

# крепим скрины выполнения кода + ссылку на гитхаб

# with open('decoded.txt', 'r') as data:
#     my_text = data.read()

# def encode_rle(ss):
#     str_code = ''
#     prev_char = ''
#     count = 1
#     for char in ss:
#         if char != prev_char:
#             if prev_char:
#                 str_code += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     return str_code

            
# str_code = encode_rle(my_text)
# print(str_code)

# with open('encoded.txt', 'r') as data:
#     my_text2 = data.read()

# def decoding_rle(ss:str):
#     count = ''
#     str_decode = ''
#     for char in ss:
#         if char.isdigit():
#             count += char 
#         else:
#             str_decode += char * int(count)
#             count = ''
#     return str_decode

# str_decode = decoding_rle(my_text2)
# print(str_decode)