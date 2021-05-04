
s=open('24.txt').readline()+'*'
c=1
m=0
for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        c+=1
        if c>m:
            m=c
    else:
        c=1
print(m)

