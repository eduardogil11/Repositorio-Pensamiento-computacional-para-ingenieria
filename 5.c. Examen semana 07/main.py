a=int(input())
b=int(input())
if a<b:
    while a<=b:
        if a%2==0:
            print (a)
        a=a+1
else:
    print ('a debe ser menor a b')