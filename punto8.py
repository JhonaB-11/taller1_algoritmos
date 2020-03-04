countPeople = 0
countPeople30and40 = 0
countPeople40and60 = 0
countPeople60 = 0

averageAge = 0
averageWeight = 0


while (True):
    age = float(input("Ingrese Edad:  "))
    weight = float(input("Ingrese Peso:  "))
    countPeople += 1
    averageAge += age
    averageWeight += weight

    #if age>=30 and age<40:
        #countPeople30and40 += 1
    #elif age>=40 and age<60:
        #countPeople40and60 += 1
    #elif age>=60:
        #countPeople60 += 1
    if age>=60:
        countPeople60 += 1
    elif age>=40:
        countPeople40and60 += 1
    elif age>=30:
        countPeople30and40 += 1

    if countPeople%5 == 0:
        stopProgram = input("Lleva " + str(countPeople) + " personas encuestadas, desea Continuar? Si o No  ")
        if stopProgram =="No":
            break        

averageAge = averageAge/countPeople
averageWeight = averageWeight/countPeople

print("Promedio de Edad:  "+str(averageAge))
print("Promedio de Peso:  "+str(averageWeight))

print("La cantidad de Personas encuestadas:  " + str(countPeople))
print("La cantidad de Personas encuestadas entre 30 y 40 son: " + str(countPeople30and40))
print("La cantidad de Personas encuestadas entre 40 y 60 son:  " + str(countPeople40and60))
print("La cantidad de Personas encuestadas mayores a 60 son:  " + str(countPeople60))

