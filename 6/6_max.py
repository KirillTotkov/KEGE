max=0
for i in range(1,1000):
    d=i
    s=0
    n=0
    while s<=365:
        s+=d
        n+=5
    if n==55:
       max=i
print(max)
