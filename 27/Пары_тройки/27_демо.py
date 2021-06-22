# 	(№ 2660) (Демовариант 2021 г.). Имеется набор данных, состоящий из пар положительных целых чисел. Необходимо
# 	выбрать из каждой пары ровно одно число так, чтобы сумма всех выбранных чисел не делилась на 3 и при этом была
# 	максимально возможной. Гарантируется, что искомую сумму получить можно. Программа должна напечатать одно число –
# 	максимально возможную сумму, соответствующую условиям задачи.
#   Входные данные. Даны два входных файла (файл A и файл B), каждый из которых содержит в первой строке количество
#   пар N (1 ≤ N ≤ 100000). Каждая из следующих N строк содержит два натуральных числа, не превышающих 10 000.
#   В ответе укажите два числа: сначала значение искомой суммы для файла А, затем для файла B.

f=open('../27_data/27-b.txt')
n=int(f.readline())
s=[0]
for _ in range(n):
    para=[int(x) for x in f.readline().split()]
    cmb=[a+b for a in s for b in para]
    cmb.sort()
    s=set(cmb[-1000:])
print(max(x for x in s if x%3!=0))





# 2 способ
# f=open('../27_data/27-a.txt')
# n=int(f.readline())
#
# def get():
#     return list(map(int, f.readline().split()))
# s=get()
#
# for i in range(n-1):
#     para=get()
#     cmb=[a+b for a in s for b in para]
#     s1=[0]*3
#     for x in cmb:
#         s1[x%3]=max(s1[x%3],x)
#     s=[x for x in s1 if x!=0 ]
#
# m=0
# for x in s:
#     if x%3!=0 and x>m:
#         m=x
# print(m)










# # 3 спомоб (только а)
# from itertools import product
# f=open('27_data/27-b.txt')
# n=int(f.readline())
# a=[[int(x)for x in f.readline().split()] for i in range(n)]
# m=0
# for x in product(*a):
#     s=sum(x)
#     if s%3!=0:
#         m=max(m,s)
# print(m)
