# № 935, Джобс 08.02.2021
# Выведите 6 чисел по порядку, начиная с 700000, таких, что количество натуральных делителей каждого следующего числа
# будет превосходить количество натуральных делителей предыдущего выведенного числа.
# В качестве ответа приведите 6 пар – найденное число и количество его натуральных делителей.

a=0
for x in range(700000,10000000):
    sq=int(x**0.5)
    d=set()
    for i in range(1, sq+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    if len(d)>a:
        print(x,len(d))
        a=len(d)