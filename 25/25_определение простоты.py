def prime(x):
    sq=int(x**0.5)
    for i in range(2,sq+1):
        if x%i==0:
            return False
    return True
print(prime(12))
print(prime(101))
