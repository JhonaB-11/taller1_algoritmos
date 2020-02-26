contMen = 0
contMay = 0
iterador = True

print("CANTIDADES MAYORES Y MENORES")

cantidades = int(input("¿Cuántos valores va a introducir? "))

if cantidades <= 0:
    print("¡Imposible!")
else:
    cantidad = 0
    for i in range(1, cantidades + 1):
        cantidadD = int(input(f"Escriba la Cantidad {i}: "))
        if cantidadD <= 0:
            contMen+=1
        elif cantidadD > 0:
            contMay+=1
    print("La menores son: "+ str(contMen)+" y las mayores cantidades son: "+str(contMay))