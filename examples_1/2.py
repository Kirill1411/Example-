# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12


# from curses.ascii import isdigit
from random import randint


list1 = [randint(0, 10) for i in range(5)]
print(list1, end=' -> ')
end_sum = 0

for i in range(len(list1)):
    if i % 2 != 0:
        end_sum += list1[i]

print(end_sum)
 
# n=[1, 2, 3, 4, 5]
# chet=[]
# nechet=[]
# for i in range(len(n)):
#     if i%2==0:
#         chet.append(n[i])
#     else:
#         nechet.append(n[i])
# print(chet, nechet)
