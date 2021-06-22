# кол-во пар произведение кратно 26
f=open('27_2.txt')
n=int(f.readline())
d=[0]*26
pair=0
for _ in range(n):
    x=int(f.readline())
    for y in range(26):
        if (x*y)%26==0:
            pair+=d[y]
    d[x%26]+=1
print(pair)