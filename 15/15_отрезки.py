
# На числовой прямой даны три отрезка: P = [10, 40], Q = [5, 15] и R = [35, 50].
# Какова наименьшая возможная длина интервала A, что формула
# ((x ∈ A) ∨ (x ∈ P)) ∨ ((x ∈ Q) → (x ∈ R))
# тождественно истина, то есть принимают значение 1 при любом значении переменной х.


def frange(start, stop):
    arr = []
    while start <= stop:
        arr.append(str(start))
        if start + 1 <= stop:
            arr.append(str(start) + '.5')
        start += 1
    return arr

p = set(frange(10, 40))
q = set(frange(5, 15))
r = set(frange(35, 50))
def f(a, x):
    return ((x in a) or (x in p)) or ((x in q) <= (x in r))

a = set()
for x in frange(1, 1000):
    if not f(a,x):
        a.add(x)
print(sorted(a))