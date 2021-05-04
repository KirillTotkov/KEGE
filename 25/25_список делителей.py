x=9
sq=int(x**0.5)
d=[]
if sq**2==x:
    d.append(sq)

for i in range(1,sq):
    if x%i==0:
        d.append(i)
        d.append(x//i)
d.sort()
print(d)
