# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11

try:
    list = input('Введите вещественное число: ')
    float(list)
except:
    print('Введенные символы не являются вещественным числом')
sum = 0
for i in range(len(list)):
    if list[i] != '.':
        sum = sum + int(list[i])
print('{} -> {}'.format(float(list), sum))
