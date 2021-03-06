# (№ 2562) (Демовариант 2021 г.). Напишите программу, которая ищет
# среди целых чисел, принадлежащих числовому отрезку [174457; 174505],
# числа, имеющие ровно два различных натуральных делителя, не считая
# единицы и самого числа. Для каждого найденного числа запишите эти два
# делителя в таблицу на экране с новой строки в порядке возрастания произведения
# этих двух делителей. Делители в строке таблицы также должны следовать в порядке возрастания.

def divizors(n):
    divizors=[1,n]
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            divizors.append(i)
            divizors.append(n//i)
    return sorted(set(divizors))

for i in range(174457, 174505):
    if len(divizors(i))==4:
        print(*divizors(i)[1:-1])
