# (№ 3774) В файле записана последовательность натуральных чисел. Гарантируется, что все числа различны.
# Из этой последовательности нужно выбрать четыре числа, чтобы их сумма делилась на 4 и была наименьшей.
# Какую наименьшую сумму можно при этом получить?
from itertools import combinations
f=open('27_data/27-55b.txt')
n=int(f.readline())
a=[int(f.readline()) for x in range(n)]
a.sort()
a=a[:100]
m=float('inf')
for x1,x2,x3,x4 in combinations(a,4):
    s=x1+x2+x3+x4
    if s%4==0:
        m=min(s,m)
print(m)