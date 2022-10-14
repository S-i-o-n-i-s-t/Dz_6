# Представлен список чисел, нужно вывести элементы исходного списка значения которых больше предидущего элемента. Use comprehension  numbers = [] for i in range(20): numbers.append(randint(-10, 10)).
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import randint

n = int(input('Введите число - '))
z = 1
v = 50
size = []
size1 = [size.append(randint(z, v)) for _ in range(n)]

print(size)

num = []
num1 = [num.append(size[x + 1]) for x in range(n - 1) if size[x] < size[x + 1]]

print(num)






exit()
n = int(input())
z = 1
v = 50
size = []
num = []
for i in range(n):
    size.append(randint(z, v))
print(size)

for x in range(n - 1):
    if size[x] < size[x + 1]:
        num.append(size[x + 1])
print(num)

# size = [] for _ in range(20): size.append(randint(z, v))
# print(size)







