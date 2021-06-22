# Сколько существует различных пятизначных чисел, записанных в восьмеричной системе счисления, в записи которых каждая 
# следующая цифры отличается от предыдущей на два?

from itertools import product
def f(p):
    return all([abs(p[i]-p[i-1])==2 for i in range(1,len(p))  ])
c=0
for p in product( [0,1,2,3,4,5,6,7,],repeat=5 ):
    if p[0]!=0 and f(p)==1:
        print(p)
        c+=1
print(c)