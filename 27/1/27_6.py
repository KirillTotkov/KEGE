# (№ 3146) Дана последовательность, которая состоит из троек натуральных чисел. Необходимо распределить все числа
# на три группы, при этом в каждую группу должно попасть ровно одно число из каждой исходной тройки. Сумма всех чисел
# в первой группе должна быть нечётной, во второй – чётной. Определите максимально возможную сумму
# всех чисел в третьей группе.
# Входные данные. Даны два входных файла (файл A и файл B), каждый из которых содержит в первой строке количество
# чисел N (1 ≤ N ≤ 100000). Каждая из следующих N строк содержит три натуральных числа, не превышающих 10000.

from itertools import permutations
f=open('../27_data/27-40a.txt')
n=int(f.readline())

def get():
    a=list(map(int,f.readline().split()))
    return list(permutations(a))
s=get()
for _ in range(n-1):
    pere=get()
    cmb=[ sorted([a[0]+b[0],a[1]+b[1],a[2]+b[2]]) for a in s for b in pere ]
    s1=[[0,0,0]]*3
    for x in cmb:
        print(cmb)
        print(x)
        print(s1)
        break
        i=x[0]%2+x[1]%2
        if x[2]>s1[i][2]:
            s1[i]=x
    s=[ x for x in s1 if x[2]!=0]
print(s[1][2])  
        
    
