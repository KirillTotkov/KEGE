# (№ 2546) (Е. Джобс) Текстовый файл 24-j5.txt
# состоит не более чем из 10**6 символов S, T, O, C, K.
# Определите максимальное количество подряд идущих комбинаций «KOT».

s=open('24data/24-j5.txt').readline()
s=s.replace('KOT','Z')
c=0
m=0
for i in range(len(s)):
    if s[i] in "Z":
        c+=1
        m=max(m,c)
    else:
        c=0
print(m)