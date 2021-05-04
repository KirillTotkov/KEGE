# 21)	Определите, сколько символов * выведет эта процедура при вызове F(28):
# def F( n ):
#   print('*')
#   if n >= 1:
#     print('*')
#     F(n-1)
#     F(n-2)

from functools import lru_cache
@lru_cache()
def f( n ):
    if n>=1:
        return 2 + f(n-1 ) + f(n-2) # 2-кол-во звездочек
    else:
        return 1
print(f(28))