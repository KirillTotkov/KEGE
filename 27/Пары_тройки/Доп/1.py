# 	(№ 2660) (Демовариант 2021 г.). Имеется набор данных, состоящий из пар положительных целых чисел.
# 	Необходимо выбрать из каждой пары ровно одно число так, чтобы сумма всех выбранных чисел не делилась
# 	на 3 и при этом была максимально возможной. Гарантируется, что искомую сумму получить можно. Программа
# 	должна напечатать одно число – максимально возможную сумму, соответствующую условиям задачи.

f=open('data/27-b.txt')
n=int(f.readline())
s=[0]
for _ in range(n):
    pair=[int(x) for x in f.readline().split()]
    cmb=[a+b for a in s for b in pair]
    s={x%3:x for x in sorted(cmb)}.values()
m= max(x for x in s if x%3!=0)
print(m)












# f=open('data/27-b.txt')
# n=int(f.readline())
# s=[0]
# for _ in range(n):
#     pair=[int(x) for x in f.readline().split()]
#     cmb=[a+b for a in s for b in pair]
#     s1=[0]*3
#     for x in cmb:
#         s1[x%3]=max(s1[x%3],x)
#     s=[x for x in s1 if x!=0]
# m=max(x for x in s if x%3!=0)
# print(m)