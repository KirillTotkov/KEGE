# предпоследней командой которых является команда «1»?
def f(a,b):
    if a>b or a==25:
        return 0
    elif a==b:
        return 1
    else:
        return f(a+1,b)+f(a*2,b)
print(f(4,11)+f(4,22))