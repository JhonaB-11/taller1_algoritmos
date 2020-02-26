print("SUMA DE CANTIDADES")

cantidad = int(input("¿Cuántos valores va a introducir? "))

if cantidad <= 0:
    print("¡Imposible!")
else:
    suma = 0
    for i in range(1, cantidad + 1):
        valor = float(input(f"Escriba la Cantidad {i}: "))
        suma = suma + valor
    print(f"La suma de las cantidades que ha escrito es {suma}")



    