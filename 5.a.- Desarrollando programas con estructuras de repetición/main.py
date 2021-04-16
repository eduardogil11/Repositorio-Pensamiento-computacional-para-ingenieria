def eleva_potencia(num,potencia):
    elevado = num ** potencia
    return elevado 

def aproximacion_PI(numero):
    n= 0
    x = 1
    k = 1
    while(k<=numero):
        n = n+(1/k*x)
        x = x*-1
        k = k+2
    return n*4 

def date_sim_pikachu(i):
    if(i== 'pikapika'):
        return 'chu'
    elif (i== 'pika!'):
        return 'pika'
    elif(i== 'pikachu'):
        return 'pikachu!!!'
    else:
        return '???'


op = int(input())
if (op==1):
    num = int(input())
    potencia = int(input())
    print("%.4f"%eleva_potencia(num,potencia))
elif (op==2):
    numero= float(input())
    print ("%.4f"%aproximacion_PI(numero))
elif (op==3):
    r = "hola"
    while(r != "pikachu!!!"):
        i = str(input())
        r = (date_sim_pikachu(i))
        print(r)