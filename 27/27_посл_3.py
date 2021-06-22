# (№ 3922) (И. Кобец) Имеется набор данных, состоящий из N различных положительных чисел. Необходимо из этих чисел
# построить самую длинную возрастающую арифметическую прогрессию c шагом от 1 до 100 включительно и вывести её длину.
# Входные данные. Даны два входных файла (файл A и файл B), каждый из которых содержит в первой строке количество
# чисел N (1 ≤ N ≤ 100000). Каждая из следующих N строк содержит одно натуральное число, не превышающее 108.

from itertools import combinations
f=open('27_data/27-62a.txt')
n=int(f.readline())
a=[int(f.readline())for x in range(n)]
a.sort()
m=0
for l in range(3,21):
    for x in combinations(a,l):
        d=x[1]-x[0]
        flag=True
        for i in range(2,len(x)):
            if x[i]-x[i-1]!=d:
                flag=False
                break
        if flag: m=l
    if m!=l:
        break
print(m)