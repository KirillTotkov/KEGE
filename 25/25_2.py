# (№ 3159) Рассмотрим произвольное натуральное число, представим его всеми 
# возможными способами в виде произведения двух натуральных чисел и найдём для 
# каждого такого произведения разность сомножителей. Например, для числа 18 
# получим: 18 = 18*1 = 9*2 = 6*3, множество разностей содержит числа 17, 7 и 3. 
# Подходящей будем называть пару сомножителей, разность между которыми не превышает 90. 
# Найдите все натуральные числа, принадлежащие отрезку [500000; 1000000], у которых 
# есть не менее трёх подходящих пар сомножителей. В ответе перечислите найденные числа 
# в порядке возрастания, справа от каждого запишите наибольший из всех сомножителей, 
# образующих подходящие пары.

for x in range(500000,1000000+1):
    sq=int(x**0.5)
    k=0
    m=0
    for i in range(sq-1,1,-1):
        if (x/i-i)>90:
            break
        if x%i==0:
            m=x//i
            k+=1
    if k==3:
        print(x,m)