#Eduardo Rodríguez Gil_A01274913
#Changelog: Se terminó de programar la dificultad intermedia y difícil, se cambió la cantidad de preguntas a 10, se añadió un contador del número de preguntas y se optimizó un poco el código.
import time
import math
import random

def goto(linenum):
    global line
    line = linenum

line = 1
while True:
    if (line == 1):
    
        correctas = 0
        fallas = 0
        nopreg = 1

        print("         //~~Bienvenido a MathWorlds Runner!~~\\  v1.1")
        time.sleep(0.8)
        print("""                 
                           ho                   
                          +MN-                  
                         .NMMd`                 
               `.........dMMMMs.........        
               `:ymNNNNNNMMMMMMNNNNNNds:`       
                  .+hNMMMMMMMMMMMMNh/.          
                    `-oMMMMMMMMMN+.             
                      oMMMMMMMMMM:              
                     -NMMMdosmMMMm`             
                    `dMdo-`  `:smMy             
                    +s-`        `:y: """)
        time.sleep(3)
        print("")
        dificultad = int(input("""Selecciona el nivel de dificultad:
1 Fácil
2 Intermedio
3 Difícil
4 Instrucciones
Ingresa aquí: """))

        if (dificultad == 1):
            time.sleep(1)
            print('')
            print('¡Has seleccionado el nivel fácil!')
            time.sleep(1.5)
            print('¡Comencemos!')
            print('')
            time.sleep(1)
            while correctas < 10:
                a = random.randrange(0,11,1)
                b = random.randrange(0,11,1)
                print("Pregunta",nopreg, ' ¿Cuánto es', a, '+', b,'?')
                respuesta = int(input())
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
            print('¡Felicidades, has ganado! Tuviste ', fallas, ' fallos.')
            print('¿Quieres volver a jugar? si/no: ')
            respuesta = (input())
            if (respuesta == "si"):
                print("Ahora pon a prueba tus habilidades con otra dificultad. ¡Suerte!")
                time.sleep(2)
                goto(1)
            else: goto(2)
    
        elif (dificultad == 2):
            time.sleep(1)
            print('')
            print('¡Has seleccionado el nivel intermedio!')
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
                            respuesta = int(input())
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
                    a = random.randrange(1,11,1)
                    b = random.randrange(1,11,1)
                    print("Pregunta",nopreg, '¿Cuánto es', a, 'x', b,'?' )
                    respuesta = int(input())
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
            print('¡Felicidades, has ganado! Tuviste ', fallas, ' fallos.')
            print("Ahora pon a prueba tus habilidades con otra dificultad. ¡Suerte!")
            print('¿Quieres volver a jugar? si/no: ')
            respuesta = (input())
            if (respuesta == "si"):
                print("Ahora pon a prueba tus habilidades con otra dificultad. ¡Suerte!")
                time.sleep(2)
                goto(1)
            else: goto(2)

        elif (dificultad == 3):
            time.sleep(1)
            print('')
            print('¡Has seleccionado el nivel dificil!')
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
                            respuesta = int(input())
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
                    a = random.randrange(1,10,1)
                    b = random.randrange(2,4,1)
                    print("Pregunta",nopreg, '¿Cuánto es', a, 'con potencia de', b,'?' )
                    respuesta = int(input())
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
            print('¡Felicidades, has ganado! Tuviste ', fallas, ' fallos.')
            print("Ahora pon a prueba tus habilidades con otra dificultad. ¡Suerte!")
            print('¿Quieres volver a jugar? si/no: ')
            respuesta = (input())
            if (respuesta == "si"):
                print("Ahora pon a prueba tus habilidades con otra dificultad. ¡Suerte!")
                time.sleep(2)
                goto(1)
            else: goto(2)
            
        elif (dificultad == 4):
            time.sleep(1)
            print('')
            print('¡Oh!, ¿Es tu primera vez aquí? ¡Ven conmigo!')
            time.sleep(1.5)
            print('¡Bien, éstas son las instrucciones para jugar!')
            print('(Puedes regresar cuando quieras)')
            print('')
            time.sleep(3)
            print("""1. Para jugar, selecciona una dificultad""")
            time.sleep(2)
            print("""2.  La dificultad 1 consiste en sólo son sumas y restas,
    La dificultad 2 consiste en sólo multiplicaciones y divisiones**
    La dificultad 3 consiste en sólo potencias y raíces**
    **Tranquilo, sólo son enteros ya que se cuenta con poco tiempo""")
            time.sleep(5)
            print("""3. Se te preguntarán 10 problemas y si contestas todas correctamente ganarás,
   si te equivocas o se te acaba el tiempo, no te preocupes, puedes seguir jugando hasta que lo logres :)""")
            time.sleep(3)
            print("")
            print("""¿Fácil, no?
    ¡Adelante! :)
    Es hora de que pongas a prueba tus habilidades. ¡Suerte!
    """)
            time.sleep(1.5)
        
            respuesta = input("""¿Quieres volver al inicio?
si/no: """)
        if (respuesta == "si" or respuesta == "sí"):
            time.sleep(2)
            goto(1)
        else: goto(2)
            
            
    elif (line==2):
        print('Nos vemos ):')
        break
