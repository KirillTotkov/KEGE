# 56)	В текстовом файле k8-18.txt находится цепочка из символов,
# в которую могут входить заглавные буквы латинского алфавита A…Z и десятичные цифры.
# Найдите длину самой длинной подцепочки, состоящей из одинаковых символов.
# Если в файле несколько подходящих цепочек одинаковой длины, нужно взять первую из них.
# Выведите сначала символ, из которого строится эта подцепочка,
# а затем через пробел – длину этой подцепочки.

s=open('24data/k8-18.txt').readline()
c=1
m=1
mch=s[0]
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        c+=1
        if c>m:
            m=c
            mch=s[i]
    else:
        c=1
print(mch,m)

