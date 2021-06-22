# (№ 2672) (Д.В. Богданов) Имеется набор данных, состоящий из положительных целых чисел. Необходимо определить
# количество пар элементов (ai, aj) этого набора, в которых 1 ≤ i < j ≤ N и произведение элементов кратно 6.

from itertools import combinations
f=open('27_data/27-12a.txt')
n=int(f.readline())
a=[int(f.readline())for x in range(n)]
k=0
for x1,x2 in combinations(a,2):
    if x1*x2%6==0:
        k+=1
print(k)