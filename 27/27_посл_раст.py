# 	(№ 2668) Имеется набор данных, состоящий из положительных целых чисел, каждое из которых не превышает 1000.
# 	Они представляют собой результаты измерений, выполняемых прибором с интервалом 1 минута. Требуется найти для
# 	этой последовательности контрольное значение – наименьшую сумму квадратов двух результатов измерений,
# 	выполненных с интервалом не менее, чем в 5 минут.

f=open('27_data/27-8a.txt')
n=int(f.readline())
a=[int(f.readline()) for x in range(n)]
m=float('inf')
for i in range(n):
    for j in range(i+1,n):
        if (j-i)>=5:
            m=min(m, a[i]**2+a[j]**2)
print(m)