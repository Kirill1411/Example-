# 2. Для натурального n создать последовательности 3n + 1.

# *Пример:*
# - Для n = 6:
# 1: 4,
# 2: 7,
# 3: 10,
# 4: 13,
# 5: 16,
# 6: 19

num = int(input('Введите число N: '))
list = [(i+1, 3*(i+1)+1) for i in range(num)]
list.sort(key=lambda x: x[1])
for i in list:
    print(i[0] ,':', i[1])
# print([(i+1, 3*(i+1)+1) for i in range(num)])
# print(list)