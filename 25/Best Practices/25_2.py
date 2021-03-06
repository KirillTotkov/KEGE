# (№ 2575) Напишите программу, которая ищет среди целых чисел, принадлежащих числовому
# отрезку [244143; 1367821], числа, имеющие ровно 5 различных делителей. В ответе для каждого
# найденного числа запишите два его наибольших делителя, не равных самому числу, в порядке возрастания.

for x in range(244143, 1367821+1):
    sq=int(x**0.5)
    if sq**2!=x: continue #оптимизация
    d=set()
    for i in range(1,sq+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    if len(d)==5:
        d=sorted(d)
        print(d[-3],d[-2])