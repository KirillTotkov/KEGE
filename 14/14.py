# (М.В. Кузнецова) Значение арифметического выражения: 9**7 - 3**10 + 3**21 – 9 записали
# в системе счисления с основанием 3. Сколько цифр «2» содержится в этой записи?

s=9**7-3**10+3**21-9
k=0
while s:
    if s%3==2:
        k=k+1
    s//=3
print(k)