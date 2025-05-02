#Ejercicio 1
lista=[]
for i in range (0,101,4):
    lista.append(i)
print(lista)


#Ejercicio 2
lista=["fuego","viento","agua","tierra","rayo"]
print (lista[-2:-1])


#Ejercicio 3
lista=[]
for i in range (0,3):
    lista.append(input("ingrese elemento "))
print (lista)


#Ejercicio 4

animales=["perro","gato","conejo","pez"]
animales[2]="loro"
animales[-1]="oso"

print (animales)

#Ejercicio 5
#En el siguiente codigo lo que hace el programa es remover de la lista "numeros" el valor máximo de todos, para eso usa la funcion max
numeros=[8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)


#Ejercicio 6

lista=[]
for i in range (10,31,5):
    lista.append(i)
print (lista)


#Ejercicio 7

autos=["sedan","polo","suran","gol"]
autos[1:3]="clio","hilux"
print(autos)


#Ejercicio 8

dobles=[]
for i in range (5,16,5):
    dobles.append(i*2)
print(dobles)


#Ejercicio 9
compras=[["pan","leche"],["arroz","fideos","salsa"],["agua"]]
print (compras)
print("-----------------------------------------------------")

#Agrega "jugo" a la lista del tercer cliente usando append
compras[2].append("jugo")

#remplaza fideos por tallarines en la lista del segundo cliente
compras[1][1]="tallarines"

#Elimina "pan" de la lista del primer cliente
compras[0].remove("pan")
print (compras)


#Ejercicio 10
lista_anidada=[15,True,[25.5,57.9,30.6],False]
print(lista_anidada)

