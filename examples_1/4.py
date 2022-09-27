# Напишите программу, которая принимает на вход число N и
# выдаёт последовательность из N членов.

# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81
#  1*-3, *-3, * -3


# def mult_3(n = int(input('Введите число N: '))):
#     numbers = [1]
#     for i in range(n):
#         num = numbers[i] * -3
#         numbers.append(num)
#     print(numbers)
        
# mult_3()


# number = int(input('Ввелите число N: '))
# numbers = [1]
# for i in range(number):
#     num = (numbers[i] * -3)
#     numbers.append(num)
# print(numbers)

number = int(input('Ввелите число N: '))
x = -3
res = list(map(lambda res: x**(res+1), [i for i in range(number)]))

print(res)
