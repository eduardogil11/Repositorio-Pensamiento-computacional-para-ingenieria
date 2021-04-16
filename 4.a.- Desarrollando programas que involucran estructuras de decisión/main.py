def corriente(voltaje,resistencia):
    corriente = (voltaje / resistencia)
    return corriente
def voltaje(corriente,resistencia):
    voltaje = corriente * resistencia
    return voltaje
def resistencia(corriente,voltaje):
    resistencia = voltaje / corriente
    return resistencia

opcion = int(input())
if opcion == 1:
    v = int(input())
    if v > 0:
        print("True")
    else:
        print("False")
elif opcion == 2:
    voltaje = float(input())
    resistencia = float(input())
    if resistencia > 0:
        print(corriente(voltaje,resistencia))
    else:
        print("-1")
    
    
elif opcion == 3:
    corriente = float(input())
    resistencia = float(input())
    print(voltaje(corriente,resistencia))

elif opcion == 4:
    corriente = float(input())
    voltaje = float(input())
    if corriente > 0:
        print(resistencia(corriente,voltaje))
    else:
        print("-1")
        
else:
    print("entrada no valida")