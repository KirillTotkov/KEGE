# Запись числа 381 в системе счисления с основанием N оканчивается
# на 3 и содержит 3 цифры. Укажите наибольшее возможное основание
# этой системы счисления N.

for n in range(2,500):
    if 381%n==3 and n**2<=381<n**3:
        print(n)