# (№ 2510) (А.М. Кабанов) В текстовом файле k7a-1.txt
# находится цепочка из символов латинского алфавита A, B, C, D, E.
# Найдите длину самой длинной подцепочки,
# состоящей из символов A, B или C (в произвольном порядке).

f=open('')
s=f.readline()+'*'
f.close()
c=0
m=0
for i in range(len(s)):
    if s[i] in 'ABC':
        c+=1
    elif c>0:
        m=max(c,m)
        c=0
print(m)


