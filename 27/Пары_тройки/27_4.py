# (№ 2689) Имеется набор данных, состоящий из троек положительных целых чисел. Необходимо выбрать из каждой тройки
# два числа так, чтобы сумма всех выбранных чисел не делилась на 5 и при этом была максимально возможной.
# Гарантируется, что искомую сумму получить можно. Программа должна напечатать одно число – максимально возможную
# сумму, соответствующую условиям задачи.
# Входные данные. Даны два входных файла (файл A и файл B), каждый из которых содержит в первой строке количество
# троек N (1 ≤ N ≤ 100000). Каждая из следующих N строк содержит три натуральных числа, не превышающих 10 000.
# В ответе укажите два числа: сначала искомое значение для файла А, затем для файла B.

f=open('../27_data/27-29a.txt')
n=int(f.readline())

def get():
    a= list(map(int,f.readline().split()))
    return [ a[0]+a[1],a[0]+a[2],a[1]+a[2] ]
s=get()
for x in range(n-1):
    pary=get()
    cmb=[a+b for a in s for b in pary]
    s1=[0]*5
    for x in cmb:
        s1[x%5]=max(s1[x%5],x)
    s=[x for x in s1 if x!=0]
print(max(s[1:]))

