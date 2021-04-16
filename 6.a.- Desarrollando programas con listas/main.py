def captura_lista (tam):
    lista = []
    for i in range (1,tam+1,1):
        num = int(input())
        lista.append(num)
    return lista

def inicializa_lista (lista,valor):
    for i in range(0,len(lista),1):
        lista[i] = valor
    return lista

def cuenta_impares (lista):
    cont = 0
    for i in range (0,len(lista),1):
        if lista[i] %2!=0:
            cont = cont+1
    return cont

def invierte_lista ():
    lista=[]
    i=0
    for i in range(tam):
        lista.append(int(input()))
    lista.reverse()
    return lista

def mayor_valor (lista):
    max = lista[0]
    for i in range (1,len(lista)):
        if lista[i] > max:
            max = lista[i]
    return max

opcion = int(input())
if opcion == 1:
    tam = int(input())
    print(captura_lista(tam))
elif opcion == 2:
    tam = int(input())
    lista = captura_lista(tam)
    valor = int(input())
    print(inicializa_lista(lista,valor))
elif opcion == 3:
    tam = int(input())
    lista = captura_lista(tam)
    print(cuenta_impares(lista))
elif opcion == 4:
    tam=int(input())
    print(invierte_lista())
elif opcion == 5:
    tam = int(input())
    if tam==0:
        print("False")
    else:
        lista = captura_lista(tam)
        print(mayor_valor(lista))