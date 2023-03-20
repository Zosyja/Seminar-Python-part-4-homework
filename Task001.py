# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. 
# n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. 

n = int(input('Введите количество элементов в первом массиве: '))
m = int(input('Введите количество элементов во втором массиве: '))

import random
first = []
for i in range(n):
    first.append(random.randint(1,10))
print(first)

import random
second = []
for i in range(m):
    second.append(random.randint(1,10))
print(second)

print(*sorted(set(first).intersection(second)))