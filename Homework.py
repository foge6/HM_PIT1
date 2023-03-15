# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
# a = int(input())
# b = int(a/100)
# c = int((a/10) % 10)
# d = a % 10
# g = b+c+d
# print(b, c, d, g)


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

# s = int(input())
# petya = int(s/6)
# sergey = int(s/6)
# kate = int(s*4/6)
# print('Петя сделал', petya, 'Сережа сделал', sergey, 'Катя сделала', kate)

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

# ticket=input()
# one=int(ticket[0])
# two=int(ticket[1])
# three=int(ticket[2])
# four=int(ticket[3])
# five=int(ticket[4])
# six=int(ticket[5])
# result_left=int(one+two+three)
# result_right=int(four+five+six)
# if result_left == result_right:
#     print('Ticket is happy!')
# else:
#     print('Ticket isn"t happy')

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

# print('Write long')
# long=int(input())           
# print('Write hight')
# hight=int(input())         
# print('How many slice')
# slice=int(input())          
# first_check = slice/long * 10
# second_check = slice/hight * 10
# if (long*hight <= slice ):
#     print('no')
# elif (long==1 and hight==slice):
#     print('no')
# elif (hight==1 and long==slice):
#     print('no')
# elif (long==1 and hight<slice):
#     print('yes')
# elif (hight==1 and long<slice):
#     print('yes')
# elif (first_check%10==0 or second_check%10==0):
#     print('yes')
# else:
#     print('no')