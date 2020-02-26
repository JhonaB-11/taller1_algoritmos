estatura = ""
promEstatura = 0
contE = 0
auxEstatura = 0
iterador  =  True

print("PROMEDIO ESTATURA")

estatura  =  int(input( "Ingrese la estatura " ))

while (estatura > 1):
    contE += 1
    auxEstatura += estatura
    promEstatura  =  auxEstatura/contE
    print("El promedio de estatura de los " + str(contE) + " estudiantes es de:" + str(promEstatura) )
    iterador = input("Continuar ? (1),Cerrar (0):  ")
    if iterador !="1":
        break
    else:
        estatura  =  int(input( "Ingrese la estatura " ))
        promEstatura  =  estatura/contE

print("El promedio de estatura de los " + str(contE) + " estudiantes es de:" + str(promEstatura) )

