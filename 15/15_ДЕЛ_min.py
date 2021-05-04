# (№ 2991) (В.Н. Шубинкин) Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится
# без остатка на натуральное число m». Для какого наименьшего натурального числа A формула
# ((ДЕЛ(x, A) ∧ ДЕЛ(x, 45)) → ДЕЛ(x, 162)) ∧ (A > 200)
#
# тождественно истинна?

from functools import lru_cache
@lru_cache()

def ДЕЛ(a, b):
    return a % b == 0


def f(x, a):
    return ((ДЕЛ(x, a) and ДЕЛ(x, 45)) <= ДЕЛ(x, 162)) and (a > 200)


for a in range(1, 1000):
    ok = True
    for x in range(1, 100000):
        if not f(x, a):
            ok = False
            break
    if ok:
        print(a)
        break
