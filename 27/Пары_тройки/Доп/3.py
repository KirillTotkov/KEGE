# № 1233, Апробация 27.04
# Имеется набор данных, состоящий из N троек натуральных чисел. Составьте сумму из N чисел, выбрав из каждой тройки
# ровно одно число так, чтобы эта сумма не делилась нацело на k = 101 и была максимально возможной. Гарантируется,
# что искомую сумму получить можно.

f=open('data/27_B.txt')
n=int(f.readline())
s=[0]
for _ in range(n):
    pair=[int(x) for x in f.readline().split()]
    cmb=[a+b for a in s for b in pair]
    s={ x%101:x for x in sorted(cmb) }.values()
m=max(x for x in s if x%101!=0)
print(m)