# 	(№ 3822) (А. Кабанов) В файле записана последовательность натуральных чисел. Гарантируется, что все числа различны.
# 	Рассматриваются всевозможные группы чисел, состоящие из любого количества элементов последовательности.
# 	Необходимо найти количество таких групп, для которых сумма элементов кратна 3.

f=open('27_data/27-58a.txt')
n=int(f.readline())
k=[0,0,0]
for _ in range(n):
    x=int(f.readline())
    k_new=[0,0,0]
    for y in range(3):
        k_new[(x+y)%3]+=k[y]
    k_new[x%3]+=1
    for y in range(3):
        k[y]+=k_new[y]
print(k[0])

