# (№ 2745) (А.Г. Минак) Рассматривается множество целых чисел, принадлежащих числовому отрезку [1031;125888],
# которые не оканчиваются цифрой 5 и являются полными квадратами. Найдите количество таких чисел и наименьшее
# такое число, оканчивающееся на 36. В ответе запишите два целых числа: сначала количество, затем наименьшее такое
# число, оканчивающееся на 36.

a = [x for x in range(1031, 125888 + 1) if x % 10 != 5 and int(x ** 0.5) ** 2 == x]
b = [x for x in a if x % 100 == 36]
print(len(a), b[0])
