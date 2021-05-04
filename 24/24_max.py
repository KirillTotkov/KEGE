# (№ 2506) В текстовом файле k7.txt находится цепочка из символов
# латинского алфавита A, B, C длиной не более 10**6 символов.
# Найдите длину самой длинной подцепочки,
# состоящей из символов C.

# 1 ВАРИАНТ
f=open('k7.txt')
s=f.readline()
f.close()
c=0
m=0
for i in range(len(s)):
    if s[i]=='C':
        c+=1
        m=max(c,m)
    else:
        c=0
print(m)

# 2 ВАРИАНТ:
f = open('k7.txt')
s = f.readline()+'*'
c = 0
m = 0
for i in range(len(s)):
    if s[i] == 'C':
        c += 1
    elif c > 0:
        m = max(c, m)
        c = 0
print(m)
