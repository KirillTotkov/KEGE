# кол-во пар  сумма четна и произведение кратно 5
f=open('')
n=int(f.readline())
d=[0]*10
pair=0
for _ in range(n):
    x=int(f.readline())
    if (x*y)%5==0 and (x+y)%2==0:
        pair+=d[y]
    d[x%10]+=1
print(pair)