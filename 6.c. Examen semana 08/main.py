def valor_max(elemento):
    valor=max(elemento)
    return valor

elemento = []
for i in range (5):
    elemento.append(int(input()))
print(valor_max(elemento))