# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится
# без остатка на натуральное число m». Для какого наибольшего натурального числа A формула
# ДЕЛ(144, A) ∧ (¬ДЕЛ(x, A) → (ДЕЛ(x, 18) → ¬ДЕЛ(x, 24)))
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?

def f(x,a):
    return (144%a==0) and ((x%a!=0)<=((x%18==0)<=(x%24!=0)))

for a in range(1,1000):
    if all(f(x,a)==1 for x in range(1,5000)):
        print(a)