from functools import lru_cache
@lru_cache()
def f(x, y):
    a = 0
    b = 0
    while x > 0 or y > 0:
        if x > 0:
            a = a + 1
        if y > 0:
            b = b + 1
        x = x // 2
        y = y // 10
    return a==6 and b==7
for x in range(1000000,2000000):
    print(x)
    for y in range(1000000,2000000):
        if f(x, y):
            print(x*y)
