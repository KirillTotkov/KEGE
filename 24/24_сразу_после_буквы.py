# (№ 3155) Текстовый файл 24-s2.txt состоит не более чем из 10**6 заглавных латинских букв.
# Определите символ, который чаще всего встречается в файле сразу после буквы A.
# В ответе запишите сначала этот символ, а потом сразу (без разделителя)
# сколько раз он встретился после буквы А. Если таких символов несколько, нужно вывести тот,
# который стоит раньше в алфавите. Например, в тексте ABCAABADDD после буквы A два раза стоит B,
# по одному разу – A и D. Для этого текста ответом будет B2.

f=open('24data/24-s2.txt')
s=f.readline()
m=0
mch=''
for i in range(ord('A'),ord('Z')+1):
    ch=chr(i)
    k=0
    for i in range(len(s)-1):
        if s[i]=='A' and s[i+1]==ch:
            k+=1
    if k>m:
        m=k
        mch=ch
print(m,mch)


