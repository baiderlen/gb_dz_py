'''
1. Вычислить число π c заданной точностью d
'''

# d = 0.001
# n = 1
# p = 4
#
# while d < abs(4/((2 * n) + 1) * (-1) ** n):
#     p += 4/((2 * n) + 1) * (-1) ** n
#     n += 1
# print(p)


'''
2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
'''

# def func(n):
#     num = []
#     d = 2
#     while d * d <= n:
#         if n % d == 0:
#             num.append(d)
#             n //= d
#         else:
#             d += 1
#     if n >= 1:
#         num.append(n)
#     return num
# print(func(int(input('Введите число: '))))


'''
3. Задайте последовательность чисел. Напишите программу, которая выведет список 
неповторяющихся элементов исходной последовательности.
'''

# a = []
# c = (input('Введите числа через пробел: ').split())
#
# for i in c:
#     d = c.count(i)
#     if d == 1:
#         a.append(i)
#
# print(a)


'''
4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
'''

# import random
# k = random.randrange(2, 5)
# x = []
# num = []
# for i in range(k+1):
#     if i == 0:
#         x.append('')
#     elif i == 1:
#         x.append('x')
#     else:
#         x.append('x^'+str(i))
#     num.append(random.randrange(101))
# eq = ''
# for i in range(1, k+2):
#     if num[-i] != 0:
#         if i != k+1:
#             eq += str(num[-i])+'*'+x[-i]+' + '
#         else:
#             eq += str(num[-i])
# eq += ' = 0'
#
# with open('DZ4(1).txt', 'w') as f:
#     f.write(eq)

'''
5 Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов.
'''

'''
я пытался, но не справился) 

with open('DZ4(1).txt', 'r') as t1, open('DZ4(2).txt') as t2, open('DZ4(3).txt', 'w') as t3:
    t1.read()
    t2.read()
    t3.write(t1.read())
    t3.write(t2.read())
    
по идее это должно записать 2 файла в новый? Не понимаю почему не записывает. 
Потом как я понимаю нужно строки преобразовать в списки, получится 2 списка из многочленов. 
Но они могут быть разными ко кол-ву коэффициентов, поэтому перебивать их нужно с конца, но так как они в виде, 
например, 23*x^2, то как их складывать?
разбивать отдельно на числа и x^2? Но не понимаю как это сделать если нам неизвестно кол-во коэффициентов.   


'''


