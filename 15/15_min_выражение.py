# Укажите наименьшее целое значение А, при котором выражение
# (xy < 4A) ∨ (x ≥ 21) ∨ (x < 4y)
# истинно для любых целых положительных значений x и y.

def f(x, y, a):
    return (x * y < 4 * a) or (x >= 21) or (x < 4 * y)
for a in range(1, 100):
    if all(f(x, y, a) == 1 for x in range(1, 100) for y in range(1, 100)):
        print(a)
        break
