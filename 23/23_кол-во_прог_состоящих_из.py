# 107)	Исполнитель Калькулятор преобразует число на экране.
# У исполнителя есть три команды, которым присвоены номера:
# 1. Прибавить 1
# 2. Прибавить 4
# 3. Умножить на 2
# Сколько существует программ, состоящих из  7 команд,
# для которых при исходном числе 3 результатом является число 27?

def f(a, b, k=0):
    if a > b:
        return 0
    elif a==b and k!=7:
        return 0
    elif a == b and k==7:
        return 1
    else:
        return f(a + 1, b, k + 1) + f(a + 4, b, k + 1) + f(a * 2, b, k + 1)
print(f(3,27))
