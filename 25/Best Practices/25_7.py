# (№ 2858) (Е. Джобс) Среди целых чисел, принадлежащих числовому отрезку [135790; 163228], найдите числа,
# сумма натуральных делителей которых больше 460000. Для каждого найденного числа запишите количество делителей
# и их сумму. В качестве делителей не рассматривать числа 1 и исследуемое число. Так, например, для числа 8 учитываются
# только делители 2 и 4.

for x in range(135790,163228+1):
    sq=int(x**0.5)
    d=set()
    for i in range(2,sq+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)

    if sum(d)>460000:
        print(len(d),sum(d))
