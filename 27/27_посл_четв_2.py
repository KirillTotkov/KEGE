# (№ 3930) (Д.Ф. Муфаззалов) В файле записана последовательность натуральных чисел. Из этой последовательности нужно
# выбрать четыре числа так, чтобы их сумма при делении на число 9 не давала остаток ноль и была наименьшей. Какова
# сумма этой четверки чисел?

f=open('27_data/27-63b.txt')
n=int(f.readline())
m=[float('inf')]*9 # минимальные числа
m2=[float('inf')]*9 # минимальные суммы пар
m3=[float('inf')]*9 # минимальные суммы троек
mn=float('inf')
for _ in range(n):
    x=int(f.readline())
    for y in range(9):
        if (x+y)%9!=0:
            mn=min(mn,x+m3[y])
    for y in range(9):
            m3[(x+y)%9]=min(m3[(x+y)%9],x+m2[y])
    for y in range(9):
        m2[(x + y) % 9]=min(m2[(x+y)%9],x+m[y])
    m[x%9]=min(m[x%9],x)
f.close()
print(mn)

from itertools import combinations
f=open('27_data/27-63b.txt')
n=int(f.readline())
a=[int(x) for x in f]
a.sort()
a=a[:100]
mn=float('inf')
for x1,x2,x3,x4 in combinations(a,4):
    s=x1+x2+x3+x4
    if s%9!=0:
        mn=min(mn,s)
print(mn)