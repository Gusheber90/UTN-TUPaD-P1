#Ejercicio1

num=0
while num <= 100:
    print (num)
    num+=1

#Ejercicio2

num=int(input("Ingrese un número entero "))
contador=0
print (type (num))
while num > 0:
    num = num//10
    contador +=1
print(f"El número ingresado tiene {contador} digitos")

#Ejercicio3

num1=int(input("Por favor ingrese un número "))
num2=int(input("Por favor ingrese otro número "))

if num1<num2:
    contador=num1
    mayor=num2
else:
    contador=num2
    mayor=num1

while contador < mayor-1:
    contador+=1
    print(contador)

#Ejercicio4

num=int(input("Ingrese un número para sumar o 0 para salir. "))
suma=num
while num!=0:
    num=int(input("Ingrese un número para sumar o 0 para salir. "))
    suma+=num
    print(suma)
print(f"La suma total fue de {suma}")

#Ejercicio5

import random
numero_aleatorio = int(random.randint(0,9))
contador=1
numero_elegido=int(input("Descubre el número mágico. Ingresa un número entre 0 y 9 "))

while numero_elegido != numero_aleatorio:
    contador+=1
    numero_elegido=int(input("Descubre el número mágico. Ingresa un número entre 0 y 9 "))
print (f"Bien hecho, necesitaste {contador} intentos para encontrar el número mágico")

#Ejercicio6
for  i  in range (100,0,-1):
    
    if (i % 2)== 0:
        print (i)
    else: continue

#Ejercicio7

num=int(input("Ingrese un número "))

suma=0
for i in range (0,num):
    suma=suma+i
  
print (suma)

#Ejercicio8

contador_par=0
contador_impar=0
positivo=0
negativo=0
#Defino el rango en el cual se repetira el bucle
for i in range (0,100):
    #Solicito al usuario que ingrese un número
    num=int(input("Ingrese un número entero "))
    #Utilizando un condicional observo si el número ingresado es par o no
    if (num % 2) == 0:
        contador_par=contador_par+1
    else:
        contador_impar= contador_impar+1
    # Y un nuevo condicional para saber si el número es positivo o no.
    if num>0:
            positivo=positivo+1
    else:
            negativo=negativo+1

print(f"Hay {contador_par} números pares, {contador_impar} números impares, {positivo} números positivos y {negativo} números negativos") 

#Ejercicio9

#la variable rango define la cantidad de números que deberá ingresar el usuario.
rango=100
suma=0
for i in range (0,rango):
     num=int(input("Por favor ingrese un número "))
     suma=suma+num

#Calculo la media sumando todos los valores ingresados en el bucle, y luego los divido por la cantidad de números.
media= suma/rango

print(f"La media es {media}")


#Ejercicio10

#En principio el número lo tomo en variable de tipo string para calcular cuantos caracteres tiene
numero=input("Ingresa un número ")
caracteres=len(numero)
#Convierto el caracter "numero" a un numero entero
numero=int(numero)
nuevo_numero=0

#Utilizo un bucle for que va de la cantidad de caracteres a 0
for i in range (caracteres,0,-1):
    #Calculo el resto de la division 
    num=numero % 10
    #
    nuevo_numero= num*10**(i-1)+nuevo_numero

    numero = numero // 10

    
print(nuevo_numero)
