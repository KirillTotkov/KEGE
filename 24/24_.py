# 91) (П.Е. Финкель, г. Тимашевск) Текстовый файл 24-1.txt
# состоит не более чем из 106 символов.
# Определите самое большое число, состоящее только из нечётных цифр.

s=open('24data/24-1.txt').readline()+'*'
c=''
m=0
for i in range(len(s)):
    if '0'<=s[i]<='9':
        c+=s[i]
    elif c!='':
        x=int(c)
        if x%2!=0 and x<m:
            m=x
        c=''
print(m)
