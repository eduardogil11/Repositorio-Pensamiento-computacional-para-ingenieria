a=int(input(' '))
b=input(' ')
matriz=[[4,9,2], [3,5,7], [8,1,6]]
contador = 0
if a==80 and b=='SING302A':
    for i in range (3):
        for j in range (3):
            if contador==3:
               print(' ')
               contador=0
            print(matriz[i][j])
            contador+=1
           