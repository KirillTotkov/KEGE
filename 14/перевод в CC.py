s=67467845
cc=6 
k=''
while s:
    k+=str(s%6)
    s//=6
print(k[::-1])
