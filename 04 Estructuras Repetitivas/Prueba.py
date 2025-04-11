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


  
 
