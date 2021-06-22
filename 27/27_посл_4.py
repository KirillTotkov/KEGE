# 	(№ 3771) В файле записана последовательность натуральных чисел. Гарантируется, что все числа различны.
# 	Из этой последовательности нужно выбрать три числа, чтобы их сумма делилась на 3 и была наибольшей.
# 	Какую наибольшую сумму можно при этом получить?

from itertools import combinations
f=open('27_data/27-52a.txt')
n=int(f.readline())
a=[int(f.readline())for x in range(n)]
a.sort()
a=a[-100:]
m=0
for x1,x2,x3 in combinations(a,3):
    s=x1+x2+x3
    if s%3==0:
        m=max(s,m)
print(m)