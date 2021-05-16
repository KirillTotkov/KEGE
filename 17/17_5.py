def f(x):
    n=str(x)
    if n.count('0')>=1 and n.count('2')>=1 and n.count('5')>=1 :
        return True
    return False

a=[x for x in range(2079,43167+1) if x%7==0 and f(x) ]
print(len(a),a[0])