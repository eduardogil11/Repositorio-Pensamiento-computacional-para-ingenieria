#Eduardo Rodríguez Gil_A01274913
#Changelog v1.5: Ahora las dificultades son basadas en personajes para más diversión,
#                se corrigió un bug a la hora de intentar salir o reiniciar el programa,
#                todavía existe un easter egg de pruebas, es posible encontrarlo por accidente, ;)
#                para usuarios de Windows, la pantalla se limpia de manera automática para evitar
#                un revolvedero de info,
#                Se añadieron créditos en la sección de Instrucciones.
#
#                Por último, un agradecimiento a todos los integrantes del equipo, al ITESM y
#                especialmente a nuestra profesora Eloína Rodriguez por hacer todo esto
#                posible!! :D

import time
import math
import random
import os

def goto(linenum):
    global line
    line = linenum

line = 1
while True:
    if (line == 1):
    
        correctas = 0
        fallas = 0
        nopreg = 1
        os.system('cls')
        print("         //~~Bienvenido a MathWorlds Runner!~~\\  v1.5")
        time.sleep(0.8)
        print("""                 
                           ho                   
           /(OnO)/        +MN-       ʕ/•ᴥ•ʔ/             
                         .NMMd`                 
               `.........dMMMMs.........        
               `:ymNNNNNNMMMMMMNNNNNNds:`       
                  .+hNMMMMMMMMMMMMNh/.          
                    `-oMMMMMMMMMN+.             
         ┌( ° ͜ʖ°)=    oMMMMMMMMMM:   ┌( ° ͜ʖ°)=          
                     -NMMMdosmMMMm`             
                    `dMdo-`  `:smMy             
                    +s-`        `:y:
               
               Dreams of our generations     """)
        time.sleep(3)
        print("")
        dificultad = int(input("""Selecciona a tu personaje:
1 Osito ʕ/•ᴥ•ʔ/         (Fácil)

2 Caballero ┌( ° ͜ʖ°)=   (Intermedio)

3 Luchador (/ •̀_•́)/     (Difícil)

4 /(OnO)/               ¿Cómo jugar?

Ingresa aquí: """))

        if (dificultad == 1):
            time.sleep(1)
            os.system('cls')
            print('')
            print('¡Has seleccionado al Osito ʕ/•ᴥ•ʔ/!')
            time.sleep(1.5)
            print('¡Comencemos!')
            print('')
            time.sleep(1)
            while correctas < 10:
                a = random.randrange(0,11,1)
                b = random.randrange(0,11,1)
                print("Pregunta",nopreg, ' ¿Cuánto es', a, '+', b,'?')
                tiempo1 = time.time()
                respuesta = int(input())
                tiempo2 = time.time()
                if tiempo2-tiempo1 < 10:
                    if (respuesta == a+b):
                        print ('¡Correcto! :D')
                        print("")
                        correctas = correctas+1
                        nopreg = nopreg+1
                    else:
                        print('¡Oh no! Está mal. La respuesta era', '',a+b,'', '):')
                        print('¡Tu puedes!, Siguiente pregunta:')
                        print('')
                        fallas = fallas+1
                        nopreg = nopreg+1
                else:
                    print('Se acabó el tiempo. ¡¡Game over!!')
                    os._exit(1)
                if respuesta == "si":
                    goto(2)
            print('¡Felicidades, has ganado! Tuviste ', fallas, ' fallos.')
            print('¿Quieres volver a jugar? si/no: ')
            respuesta = (input())
            if (respuesta == "si" or respuesta == "sí" or respuesta == "Sí" or respuesta == "SI" or respuesta =="Si"):
                print("Ahora pon a prueba tus habilidades con otra dificultad. ¡Suerte!")
                time.sleep(2)
                goto(1)
            else: goto(2)
    
        elif (dificultad == 2):
            time.sleep(1)
            os.system('cls')
            print('')
            print('¡Has seleccionado al Caballero ┌( ͝° ͜ʖ͡°)=!')
            time.sleep(1.5)
            print('¡Comencemos!')
            print('')
            time.sleep(1)
            while correctas < 10:
                operador = random.randrange(1,3,1)
                if (operador == 1):
                    verificación = 0
                    while verificación<1:
                        a = random.randrange(10,210,1)
                        b = random.randrange(2,11,1)
                        if a%b == 0:
                            print("Pregunta",nopreg, '¿Cuánto es', a, '÷', b,'?' )
                            tiempo1 = time.time()
                            respuesta = int(input())
                            tiempo2 = time.time()
                            if tiempo2-tiempo1 < 10:
                                if (respuesta == a//b):
                                    print ('¡Correcto! :D')
                                    print("")
                                    correctas = correctas+1
                                    verificación=1
                                    nopreg = nopreg+1
                                else:
                                    print('¡Oh no! Está mal. La respuesta era', '',a//b,'', '):')
                                    print('¡Tu puedes!, Siguiente pregunta:')
                                    print('')
                                    fallas = fallas+1
                                    verificación = 1
                                    nopreg = nopreg+1
                            else:
                                print('Se acabó el tiempo. ¡¡Game over!!')
                                os._exit(1)
                else:
                    a = random.randrange(1,11,1)
                    b = random.randrange(1,11,1)
                    print("Pregunta",nopreg, '¿Cuánto es', a, 'x', b,'?' )
                    tiempo1 = time.time()
                    respuesta = int(input())
                    tiempo2 = time.time()
                    if tiempo2-tiempo1 < 10:
                        if (respuesta == a*b):
                            print ('¡Correcto! :D')
                            print("")
                            correctas = correctas+1
                            nopreg = nopreg+1
                        else:
                            print('¡Oh no! Está mal. La respuesta era', '',a*b,'', '):')
                            print('¡Tu puedes!, Siguiente pregunta:')
                            print('')
                            fallas = fallas+1
                            nopreg = nopreg+1
                    else:
                        print('Se acabó el tiempo. ¡¡Game over!!')
                        os._exit(1)
            print('¡Felicidades, has ganado! Tuviste ', fallas, ' fallos.')
            print("Ahora pon a prueba tus habilidades con otra dificultad. ¡Suerte!")
            print('¿Quieres volver a jugar? si/no: ')
            respuesta = (input())
            if (respuesta == "si" or respuesta == "sí" or respuesta == "Sí" or respuesta == "SI" or respuesta =="Si"):
                print("Ahora pon a prueba tus habilidades con otra dificultad. ¡Suerte!")
                time.sleep(2)
                goto(1)
            else: goto(2)

        elif (dificultad == 3):
            time.sleep(1)
            os.system('cls')
            print('')
            print('¡Has seleccionado al Luchador (/ •̀_•́)/!')
            time.sleep(1.5)
            print('¡Comencemos!')
            print('')
            time.sleep(1)
            while correctas < 10:
                verificación = 0
                operador = random.randrange(1,3,1)
                if (operador == 1):
                    while verificación<1:
                        a = random.randrange(4,101,1)
                        b = "%.0f"%math.sqrt(a)
                        if float("%.1f"%math.sqrt(a)) == float(b):
                            print("Pregunta",nopreg, '¿Cuánto es la raíz cuadrada de', a, '?' )
                            tiempo1 = time.time()
                            respuesta = int(input())
                            tiempo2 = time.time()
                            if tiempo2-tiempo1 < 10:
                                if (respuesta == int(b)):
                                    print ('¡Correcto! :D')
                                    print("")
                                    correctas = correctas+1
                                    verificación = 1
                                    nopreg = nopreg+1
                                else:
                                    print('¡Oh no! Está mal. La respuesta era', '',b,'', '):')
                                    print('¡Tu puedes!, Siguiente pregunta:')
                                    print('')
                                    fallas = fallas+1
                                    verificación = 1
                                    nopreg=nopreg+1
                            else:
                                print('Se acabó el tiempo. ¡¡Game over!!')
                                os._exit(1)
                else:
                    a = random.randrange(1,10,1)
                    b = random.randrange(2,3,1)
                    print("Pregunta",nopreg, '¿Cuánto es', a, 'con potencia de', b,'?' )
                    tiempo1 = time.time()
                    respuesta = int(input())
                    tiempo2 = time.time()
                    if tiempo2-tiempo1 < 10:
                        if (respuesta == a**b):
                            print ('¡Correcto! :D')
                            print("")
                            correctas = correctas+1
                            nopreg=nopreg+1
                        else:
                            print('¡Oh no! Está mal. La respuesta era', '',a**b,'', '):')
                            print('¡Tu puedes!, Siguiente pregunta:')
                            print('')
                            fallas = fallas+1
                            nopreg=nopreg+1
                    else:
                        print('Se acabó el tiempo. ¡¡Game over!!')
                        os._exit(1)
            print('¡Felicidades, has ganado! Tuviste ', fallas, ' fallos.')
            print("Ahora pon a prueba tus habilidades con otra dificultad. ¡Suerte!")
            print('¿Quieres volver a jugar? Si / No: ')
            respuesta = (input())
            if (respuesta == "si" or respuesta == "sí" or respuesta == "Sí" or respuesta == "SI" or respuesta =="Si"):
                print("Ahora pon a prueba tus habilidades con otra dificultad. ¡Suerte!")
                time.sleep(2)
                goto(1)
            else: goto(2)
            
        elif (dificultad == 4):
            time.sleep(1)
            os.system('cls')
            print('                  ~¿Cómo jugar?~ \n')
            print('¡Oh!, ¿Es tu primera vez aquí? ¡Ven conmigo!')
            time.sleep(1.5)
            print('¡Bien, éstas son las instrucciones para jugar!')
            print('(Puedes regresar cuando quieras)')
            print('')
            time.sleep(3)
            print("""1. Para jugar, selecciona una dificultad""")
            time.sleep(2.5)
            print("""2.  La dificultad 1 consiste en sólo son sumas y restas,
    La dificultad 2 consiste en sólo multiplicaciones y divisiones**
    La dificultad 3 consiste en sólo potencias y raíces**
    **Tranquilo, sólo son enteros ya que se cuenta con poco tiempo""")
            time.sleep(6.5)
            print("""3. Se te preguntarán 10 problemas y si contestas todas correctamente ganarás,
    si te equivocas no te preocupes, puedes seguir jugando hasta que lo logres :), pero cuidado,
    si se te acaba el tiempo no podrás seguir!! ):""")
            time.sleep(3.5)
            print("")
            print("""¿Fácil, no?
    ¡Adelante! :)
    Es hora de que pongas a prueba tus habilidades. ¡Suerte!
    """)
            time.sleep(2)
        
            respuesta = input("""¿Quieres volver al inicio? (Escribe créditos si quieres verlos)
Sí / No: """)
        
        elif(dificultad == 5):
            time.sleep(1)
            os.system('cls')
            opcion = int(input("""
¿Qué tipo de cosa quieres hacer?
1. Cuadrito de estrellitas
2. Escalera de estrellitas
3. Pirámide horizontal de números
4. La pirámide de pascal
"""))
            if opcion==1:
                for linea in range(1):
                    for columna in range (4):
                        print("*", end="")
                    print (end="\n")
                    for columna in range (2):
                        print("*", " ", end="")
                    print (end="\n")
                    for columna in range (4):
                        print("*", end="")
                    print (end="\n")
                print("\n")
            elif opcion==2:
                depth = int(input("""¿Cuántos renglones quieres hacer?:
 """))
                for y in range(depth+1):
                    for ws in range(depth + y - depth):
                        print("* ", end = '')
                    print()
            elif opcion==3:
                depth = int(input("""¿Cuántos renglones quieres hacer?:
"""))
                a=0
                for y in range(depth+1):
                    for ws in range(depth + y - depth):
                        print(a, "", end = '')
                    a=a+1
                    print()
                for y in range(depth-1):
                    for ws in range(depth - y-1):
                        print(a, "", end = '')
                    a=a+1
                    print()
            elif opcion==4:
                renglones = int(input("""¿Cuántos renglones quieres hacer?:
 """))
                for y in range(renglones + 1):
                    for espacios in range(renglones - y + 1):
                        print("  ", end = '')
                    
                    for x in range(y + 1):
                        if x == 0 or y == 0:
                            count = 1
                        else:
                            count = int(count * (y - x + 1) / x)
                        c = str(count).rjust(3, ' ')
                        print(f"{c} ", end = '')
                    print()
            respuesta = input("""Listo
¿Quieres volver al inicio?
Sí / No: """)

        
        if (respuesta == "si" or respuesta == "sí" or respuesta == "Sí" or respuesta == "SI" or respuesta =="Si"):
            time.sleep(2)
            goto(1)
        elif (respuesta =="Créditos" or respuesta == "Creditos" or respuesta == "creditos" or respuesta == "créditos"):
            os.system('cls')
            print ("""         Gracias por visitar la sección de créditos, estamos muy felices de que alguien los vea :D

Este proyecto comenzó el 5 de Septiempre de 2019 y fue finalizado el 20 de Octubre del 2019, se nos impartió una
materia de programación en Python y gracias a ello fue posible la creación de todo esto. El proyecto fue realizado
por:    A01706155 Manolo Ramírez Pintor - Programador principal
        A01351361 Erick Gerardo Calderón Reyes - Sub programador y ayudante
        A01706083 Emiliano Mendoza Nieto - Ideas, Sub programador y corregidor de bugs
        A01274913 Eduardo Rodríguez Gil - Ideas de programación y tester
        A01706777 Jesús Ernesto García Arriola - Sub programador y debugger

¡Un agradecimiento al ITESM y especialmente a nuestra profesora Eloína Rodriguez por hacer todo esto posible!

                                                    ¡Gracias! :D""")
            variablequenohacenada = input("""
Escribe fin para salir
""")
            time.sleep(0.5)
            
        else: goto(2)
            
            
    elif (line==2):
        print('Nos vemos ):')
        break