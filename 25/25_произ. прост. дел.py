# (№ 2600) Среди целых чисел, принадлежащих числовому отрезку [268312;336492], 
# найдите числа, которые представляют собой произведение двух различных простых делителей. 
# Запишите в ответе количество таких чисел и минимальное их них.

def prime(x):
    sq=int(x**0.5)
    for i in range(2,sq+1):
        if x%i==0:
            return False
    return True
k=0
m=10**6
for x in range(268312,336492+1):
    sq=int(x**0.5)
    d=[]
    if sq**2==x:
        d+=[sq]
    for i in range(2,sq+1):
        if x%i==0:
            d+=[i,x//i]
    dp=[x for x in d if prime(x)]
    if len(dp)==2 and dp[0]*dp[1]==x:
        k+=1
        m=min(m,x)
print(k,m)
    