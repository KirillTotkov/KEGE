# (№ 2507) В текстовом файле k8.txt находится цепочка из
# не более чем 10**6 символов, в которую могут входить
# заглавные буквы латинского алфавита A…Z и десятичные цифры.
# Найдите длину самой длинной подцепочки, состоящей из одинаковых
# символов. Выведите сначала символ, из которого строится цепочка,
# а затем через пробел – длину этой цепочки. Если таких цепочек (максимальной длины)
# несколько, выведите информацию о первой встретившейся цепочке.

f = open('k8.txt')
s = f.readline()
f.close()
c = 1
m = 1
ch = 0
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        c += 1
        if c > m:
            m = c
            ch = s[i]
    else:
        c = 1
print(ch, m)
