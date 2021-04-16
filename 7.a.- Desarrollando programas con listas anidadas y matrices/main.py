def lista_anidada(exterior,interior):
    matriz=[]
    for no_ren in range(0,exterior,1):
        renglon=[]
        for no_col in range(0,interior,1):
            num=int(input())
            renglon.append(num)
        matriz.append(renglon)
    return matriz

def suma_diagonal(matriz):
    suma=0
    no_ren=0
    for renglon in matriz:
        no_col=0
        for columna in renglon:
            if no_ren == no_col:
                suma=suma+columna
            no_col=no_col+1
        no_ren=no_ren+1
    return suma

def suma_inversa(matriz):
    suma=0
    no_ren=0
    matriz=matriz[::-1]
    for renglon in matriz:
        no_col=0
        for columna in renglon:
            if no_ren==no_col:
                suma=suma+columna
            no_col=no_col+1
        no_ren=no_ren+1
    return suma

def encuentra_grupo(matriz,nombre):
    res=0
    for renglon in matriz:
        for columna in renglon:
            if columna == nombre:
                print(renglon)
                res=1
                break
    if res==0:
        print("el nombre no es epico")
        
opcion=int(input())
if opcion ==1:
    exterior=int(input())
    interior=int(input())
    print(lista_anidada(exterior,interior))
elif opcion==2:
    exterior=int(input())
    interior=int(input())
    if exterior !=interior:
        print(False)
    else:
        matriz=lista_anidada(exterior,interior)
        print(suma_diagonal(matriz))
elif opcion==3:
    exterior=int(input())
    interior=int(input())
    if exterior!= interior:
        print(False)
    else:
        matriz=lista_anidada(exterior,interior)
        print(suma_inversa(matriz))
elif opcion==4:
    nombres_epicos_geekdom =[
     ["Naofumi", "Filo", "Raphtalia"], 
     ["Rand Al'thor", "Perrin Arabaya", "Mathrim Cauldron", "Egwene Al'vere", "Nynaieve Al'mere"], 
     ["Lithany of Fury", "Macragge's Honour", "Vengeful Spirit", "Harbinger of Doom", "Chronicle of Ashes"],
     ["Cloud Strife", "Sephiroth", "Vincent Valentine", "Zack Fair", "Aerith Gainsborough", "Tifa Lockhart", "Barret Wallace", "Yuffie Kisaragi"],
     ["Cormyr", "WestGate", "Suzeil", "Menzoberranzan", "Waterdeep"],
     ["Atlas", "Dectective Comics", "Dark Horse", "Image"],
     ]
    nombre=input()
    encuentra_grupo(nombres_epicos_geekdom,nombre)