# (№ 3772) В файле записана последовательность натуральных чисел. Гарантируется, что все числа различны.
# Найдите кол-во троек различных чисел, сумма которых кратна 3
# Какую наименьшую сумму можно при этом получить?

f=open('27_data/27-53a.txt')
n=int(f.readline())
d=[0]*3 # кол-во предыдущих чисел
d2=[0]*3 #  кол-во предыдущих пар
k=0
for _ in range(n):
    x=int(f.readline())
    for y in range(3):
        if (x+y)%3:
            k+=d2[y]
    for y in range(3):
        d2[(x+y)%3]+=d[y]
    d[x%3]+=1
f.close()
print(k)

# кол-во четверок различных чисел, сумма которых кратна 3

f=open('27_data/27-53a.txt')
n=int(f.readline())
d=[0]*3
d2=[0]*3
d3=[0]*3
k=0
for _ in range(n):
    x=int(f.readline())
    for y in range(3):
        if (x+y)%3==0:
            k+=d3[y]
    for y in range(3):
            d3[(x+y)%3]+=d2[y]
    for y in range(3):
        d2[(x+y)%3]+=d[y]
    d[x%3]+=1
print(k)
