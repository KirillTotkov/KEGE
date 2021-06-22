# (№ 2673) Имеется набор данных, состоящий из положительных целых чисел. Необходимо определить количество пар
# элементов (ai, aj) этого набора, в которых 1 ≤ i + 7 ≤ j ≤ N и произведение элементов кратно 14.

f=open('27_data/27-13a.txt')
n=int(f.readline())
a=[int(f.readline())for x in range(n)]
k=0
for i in range(n):
    for j in range(n):
        if i + 7 <= j and a[i]*a[j]%14==0:
            k+=1
print(k)