# (369) На числовой прямой даны два отрезка: P=[5,30] и Q=[14,24].
# Укажите наибольшую возможную длину такого отрезка A, что формула
# ((x ∈ P) ≡ (x ∈ Q)) → (x ∉ A)
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.

def frange(start, stop):
    arr = []
    while start <= stop:
        arr.append(str(start))
        if start + 1 <= stop:
            arr.append(str(start) + '.5')
        start += 1
    return arr

p = set(frange(5, 30))
q = set(frange(14, 24))

def f(x,a):
    return ((x in p)==(x in q))<=(x not in a)
a = set()
for x in frange(1, 1000):
    if not f(a,x):
        a.add(x)
print(sorted(a))