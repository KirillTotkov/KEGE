# 	(№ 2748) (А.Г. Минак) Рассматривается множество целых чисел, принадлежащих числовому отрезку [5903; 174203],
# 	которые имеют все различные цифры, и при этом имеют в своей записи ровно три цифры большие 4. Найдите количество
# 	таких чисел и такое число наиболее близкое к 30000. В ответе запишите два целых числа: сначала количество, затем
# 	такое число наиболее близкое к 30000.

def f(x):
    s = set(str(x))
    if len(str(x)) == len(s):
        return True
def g(x):
    k = 0
    for i in str(x):
        if int(i) > 4:
            k += 1
    if k == 3:
        return True
a = [x for x in range(5903, 174203 + 1) if f(x) and g(x)]
b = [x for x in a if x < 30000]
print(len(a), b[-1])
