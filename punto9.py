numberHost = int(input("Ingrese Número de Personas:  "))
numberDays = int(input("Ingrese Número de días:  "))

totalPay = 0.0

if numberHost == 1:
    totalPay = 2500*1.19*0.95*numberDays
elif numberHost == 2:
    totalPay = 4600*1.19*0.91*numberDays
elif numberHost == 3:
    totalPay = 5200*1.19*0.85*numberDays
    
print("Total a Pagar es: "+ str(totalPay))         