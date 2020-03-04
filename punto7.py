#operaciones con listas
list1 = ['eat',3,'sun']
list2 = [2,3,4,5]
#suma de listas
newList = list1 + list2
print(newList)
#repetir lista n veces
print(list1*3)
#rebanado de listas
list3 = list1[0:2]
print(list3)
#ordenar lista de menor a mayor
list4 = ['d','a','c','b','e']
list4.sort()
print(list4)
#eliminando elemento de la lista
list4.pop(2)
print(list4)
#eliminar elemento de la lista sin retornar el valor removido
del list4[1]
print(list4)
#eliminar elemento sin conocer su posicion, conociendo el elemento a eliminar
list4.remove('d')
print(list4)
list5 = ['a','a','b','b','c']
list5.remove('a')
print(list5)
#len devuelve el numero de posicion de elementos en la lista
list6 = ['a','a','a','b','c','a','d']
for i in range(0,len(list6)):
    print(i)
#muestra los valores de la lista donde i es igual a todos los elementos de la lista
for i in list6:
    print(i)
#ejercicio para eliminiar con los dos estilos de for
list7=['a','b','a','d','a','f','a']
for i in list7:
    if i == 'a':
        list7.remove(i)
print(list7)

list8=['a','a','a','x','a','a','a']
 
pos = 0
while pos < len(list8):
    if list8[pos] == 'a':
        del list8[pos]
    else:
        pos += 1
print(list8)

pal = "palabra"
contP = 0
contL = 0
for i in range(0,len(pal)):
    for j in range(0,len(pal)):
        if j+1 > len(pal):    
            if pal[i] == pal[j+1]:
                contP += 1
            if contP>0:
                break
print("Hay letras repetidas")

#cuenta elementos de una lista o string
#entrada=input("Introduce una Palabra o Texto: ")
pal = 'roto'
palabra={}
 
for i in pal:
    if i in palabra:
        palabra[i]=palabra[i]+1
    else:
        palabra[i]=1
 
print(palabra)




    

        

