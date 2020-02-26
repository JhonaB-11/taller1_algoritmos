print("PARES Y MULTIPLICACION")

cont = 0

for num in range(0,101):
    if num%2 == 0:
        print ("Este numero es par "+str(num)+", su multiplicacion es: "+str(num*cont))
    if num%2 != 0:
        print ("Este numero es inpar "+str(num)+", su multiplicacion es: "+str(num*cont))
    cont+=1