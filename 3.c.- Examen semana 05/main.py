a = int(input())
b = int(input())
c = int(input())


def promedio (a,b,c):
    promedio = (a+b+c)/3
    return promedio

def varianza (a,b,c):
    prom = (a+b+c)/3
    varianza = ((prom - a)**2 + (prom - b)**2 + (prom - c)**2)/(3 - 1)
    return varianza

print(promedio(a,b,c))
print(varianza(a,b,c))
