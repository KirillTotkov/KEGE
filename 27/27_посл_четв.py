# кол-во четверок различных чисел, произведение котрорых кратно 24

f=open('27_data/27-53a.txt')
n=int(f.readline())
d=[0]*24
d2=[0]*24
d3=[0]*24
k=0
for _ in range(n):
    x=int(f.readline())
    for y in range(24):
        if (x*y)%24==0:
            k+=d3[y]
    for y in range(24):
            d3[(x*y)%24]+=d2[y]
    for y in range(24):
            d2[(x*y)%24]+=d[y]
    d[x%24]+=1
print(k)