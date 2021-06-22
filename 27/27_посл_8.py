# кол-во пар произведение кратно 13
f=open('27_1.txt')
n=int(f.readline())
d=[0]*13
pair=0
for _ in range(n):
    x=int(f.readline())
    for y in range(13):
        if (x*y)%13==0:
            pair+=d[y]
    d[x%13]+=1
print(pair)