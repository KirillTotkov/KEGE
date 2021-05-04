# Определите сумму чисел, которые выведет процедура при вызове F(50)
# def F( n ):
#   print(2*n+1)
#   if n > 1:
#     print(3*n-8)
#     F(n-2)
#     F(n-4)

from functools import lru_cache
@lru_cache()
def f(n):
    if n>1:
        return 2*n+1+3*n-8+f(n-2)+f(n-4)
    else:
        return 2*n+1
print(f(50))