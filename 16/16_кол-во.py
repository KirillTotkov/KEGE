# 61)	Алгоритм вычисления функции F(n) задан следующими соотношениями:
# 		F(n) =  n · n + 3 · n + 9, при n <= 15
# 		F(n) = F(n–1) + n – 2, при n > 15, кратных 3
# 		F(n) = F(n–2) + n + 2, при n > 15, не кратных 3
# Определите количество натуральных значений n из отрезка [1; 1000], для которых все цифры значения F(n) чётные.
def F(n):
    if n <= 15:
        return n ** 2 + 3 * n + 9
    elif n > 15 and n % 3 == 0:
        return F(n - 1) + n - 2
    elif n > 15 and n % 3 != 0:
        return F(n - 2) + n + 2
count = 0
for i in range(1, 1000 + 1):
    s = str(F(i))
    k = 0
    for x in s:
        if int(x) % 2 == 0:
            k += 1
    if k == len(s):
        count += 1

print(count)
