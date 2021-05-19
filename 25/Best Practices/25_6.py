#(№ 2837) (Е. Джобс) Напишите программу, которая ищет среди целых чисел, принадлежащих числовому
# отрезку [25317; 51237], которые имеют хотя бы 6 различных простых делителей. Делители 1 и само число
# не учитываются. Запишите в ответе для каждого найденного числа само число и его максимальный простой делитель.

def prime(x):
    sq=int(x**0.5)
    for i in range(2,sq+1):
        if x%i==0:
            return False
    return x>1

for x in range(25317, 51237+1):
    sq=int(x**0.5)
    d=set()
    for i in range(2,sq+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    d=[x for x in d if prime(x)]
    if len(d)>=6:
        print(x,max(d))