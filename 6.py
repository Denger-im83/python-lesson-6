### Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# a1= int(input("Введите значение 1-го элемента:"))
# d=int(input("Введите разность элементов:"))
# n=int(input("Введите количество элементов:"))
# res = [a1 + (i - 1) * d for i in range(1, n + 1)]
# print(*res)


#Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
arr = []
for i in range(20):
	x = int(random.random()*10)  
	arr.append(x)
	print("%3d" % x, end='')
	if (i+1) % 10 == 0:	print()
 
minimum = int(input('min: '))
maximum = int(input('max: '))
 
index = []
i = 0
for i in arr:
	if minimum <= i <= maximum:
		index.append(arr.index(i))
print("Количество: ", len(index))
print("Индексы: ", index)