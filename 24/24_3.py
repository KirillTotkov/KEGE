# 28)	 (А.М. Кабанов) В текстовом файле k7b-2.txt находится цепочка
# из символов латинского алфавита A, B, C, D, E, F. Найдите
# максимальную длину цепочки вида DBAC DBACDBAC....
# (состоящей из фрагментов DBAC, последний фрагмент может быть неполным).

s=open('24data/k7b-2.txt').readline()
c=0
m=0
for i in range(len(s)):
    if (s[i]=='D' and c%4==0) or (s[i]=='B' and c%4==1) or (s[i]=='A' and c%4==2) or (s[i]=='C' and c%4==3):
        c+=1
        m=max(c,m)
    elif s[i]=='D':
        c=1
    else:
        c=0
print(m)