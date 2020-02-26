numberAlumns = 0
average = 0
print("PROMEDIO EDAD")

while True:
    age = int(input("Ingrese Edad:   "))
    if age > 18:
        print("Promedio  " + str(average/numberAlumns))
        claseProgram = input("Continuar ? (1),Cerrar (0):  ")
        if claseProgram !="1":
            break
    else:
        average=average + age
        numberAlumns +=1
print("Promedio  " + str(average/numberAlumns))
        
