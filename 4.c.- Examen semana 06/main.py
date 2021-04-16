sueldo=int(input())
extras=int(input())
if(extras<=9 and extras>0):
    res=sueldo*extras*2
elif(extras<1):
    res=0
else:
    res=sueldo*9*2+(extras-9)*sueldo*3


print("$%.2f" %res)
 