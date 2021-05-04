# из 2 в 14 и содержит 6 или 10 но не оба сразу:
# 1) содержит 6 не содержит 10 - 1 программа
# 2) содержит 10 не содержит 6 - 2 программа
def f(a,b):
    if a>b or a==10:
        return 0
    elif a==b:
        return 1
    else:
        return f(a+1,b)+f(a*2,b)+f(a+3,b)
e = f(2,6)*f(6,14)

def f(a,b):
    if a>b or a==6:
        return 0
    elif a==b:
        return 1
    else:
        return f(a+1,b)+f(a*2,b)+f(a+3,b)
c = f(2,10)*f(10,14)

print(e+c)
