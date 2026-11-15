contador = 0
numero = int(input("Ingres un numero positivo:"))

while(numero != 0):
    if(numero > 0):
        contador += numero
    numero = int(input("Ingrese nuevamente otro numero positivo:"))
print(contador)