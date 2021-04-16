#Eduardo Rodríguez Gil_A01274913
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

        print("         //~~Bienvenido a MathWorlds Runner!~~\\")
        time.sleep(0.8)
        print("""                   .`                   
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
            while correctas < 6:
                a = random.randrange(1,6,1)
                b = random.randrange(1,6,1)
                print('¿Cuánto es', a, '+', b,'?' )
                respuesta = int(input())
                if (respuesta == a+b):
                    print ('¡Correcto! :D')
                    print("")
                    correctas = correctas+1
                else:
                    print('¡Oh no! Está mal. La respuesta era', '',a+b,'', '):')
                    print('¡Tu puedes!, Siguiente pregunta:')
                    print('')
                    fallas = fallas+1
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
            while correctas < 6:
                a = random.randrange(1,10,1)
                b = random.randrange(1,10,1)
                print('¿Cuánto es', a, '*', b,'?' )
                respuesta = int(input())
                if (respuesta == a*b):
                    print ('¡Correcto! :D')
                    print("")
                    correctas = correctas+1
                else:
                    print('¡Oh no! Está mal. La respuesta era', '',a*b,'', '):')
                    print('¡Tu puedes!, Siguiente pregunta:')
                    print('')
                    fallas = fallas+1
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
            print('¡Has seleccionado el nivel intermedio!')
            time.sleep(1.5)
            print('¡Comencemos!')
            print('')
            time.sleep(1)
            while correctas < 6:
                a = random.randrange(1,25,1)
                b = random.randrange(1,5,1)
                print('¿Cuánto es', a, '÷', b,'?' )
                respuesta = int(input())
                if (respuesta == a//b):
                    print ('¡Correcto! :D')
                    print("")
                    correctas = correctas+1
                else:
                    print('¡Oh no! Está mal. La respuesta era', '',a+b,'', '):')
                    print('¡Tu puedes!, Siguiente pregunta:')
                    print('')
                    fallas = fallas+1
            print('¡Felicidades, has ganado! Tuviste ', fallas, ' fallos.')
            print("Ahora pon a prueba tus habilidades con otra dificultad. ¡Suerte!")
            
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
    La dificultad 2 consiste en sumas, restas, multiplicaciones y divisiones*
    La dificultad 3 consiste en todo lo anterior, pero se añade potencias y raíces*
    **Sólo en enteros ya que se cuenta con poco tiempo""")
            time.sleep(5)
            print("""3. Se te preguntarán 6 problemas y si contestas todas correctamente ganarás,
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