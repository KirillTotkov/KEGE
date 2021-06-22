# кол-во пар с четной суммой
from itertools import combinations
f=open('27.txt')
n=int(f.readline())
d=[0]*2
pair=0
for _ in range(n):
    x=int(f.readline())
    for y in range(2):
        if (x+y)%2==0:
            pair+=d[y]

    d[x%2]+=1
print(pair)
