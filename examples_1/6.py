text = '''
Ехал Грека через реку.
Видит Грека в реке рак.
Сунул в реку руку Грека.
Рак за руку Греку цап.'''

li = list(enumerate([i for i in text.split()]))
print(li)
liU = list(filter(lambda x: x[1][0].isupper(), li))
print(liU)
liU.sort(key=lambda x: x[1])
for i in liU:
    print(i[0], '-', i[1])