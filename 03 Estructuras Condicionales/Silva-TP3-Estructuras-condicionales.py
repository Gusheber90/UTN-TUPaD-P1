#Ejercicio-1
edad= int(input("Ingrese su edad: "))
if edad> 18 : 
    print("Es mayor de edad")

#Ejercicio-2
nota=float(input("Por favor ingrese su nota: "))

if nota>=6:
    print("APROBADO")
else:
    print("DESAPROBADO")

#Ejercicio3
numero=int(input("por favor ingrese un número par: "))

if (numero % 2) == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Ejercicio4
edad=int(input("Por favor ingrese su edad "))

if edad>=18 and edad<30 :
    print("Eres un Adulto/a joven")
elif edad>=12 and edad<18:
    print("Eres un adolescente")
elif edad<12:
    print("Eres un niño/a")
else:
    print("Eres un Adulto/a")

#Ejercicio5
contraseña=len(input("Ingrese una contraseña de entre 8 a 14 caracteres: "))

if contraseña >= 8 and contraseña<= 14:
    print("Ha ingresado una contraseña correcta")
else: 
    print("Por favor, ingrese una contraseña correcta")

#Ejercicio7
palabra=input("Ingrese una frase o palabra ")
#Para conseguir la ultima letra uso len para saber de cuantos caracteres está formada la palabra y le resto 1 para despues obtener el resultado de la ultima posicion de la misma.

cantidad_letra=len(palabra)-1
ultima_letra=palabra[cantidad_letra]
#utilizo un print para ver si obtengo la ultima letra de la frase o palabra, solo a modo informativo. 
print (ultima_letra)

#creo una lista que contiene las vocales para comparar la ultima letra con los elementos de la lista y saber si es vocal o no.
vocales= ["a","e","i","o","u"] 

#Ahora utilizo un If para identificar si la ultima letra está dentro de los elementos de la lista. 
if ultima_letra in vocales:
    print(f"{palabra}!")
else:
    print(palabra)


#Ejercicio8

#pido al usuario que ingrese su nombre seguido de la opcion
nombre=input("Ingrese su nombre seguido de la opcion correcta(1,2,3) ")

#Obtengo la cantidad de caracteres utilizados para identificar cual fue el último
caracteres=(len(nombre))-1

#Convierto el último caracter a número para luego compararlo con las opciones de mi diccionario
ultimo_caracter=int(nombre[caracteres])
print (ultimo_caracter)

#Redefino la cadena nombre para que quede solo el nombre y desaparezca el número. 
nombre=nombre[0:caracteres]

#Creo un diccionario donde según la opción elegida por el usuario realizara la operación correspondiente
opciones= {
    1: nombre.upper(),#Convierte todo a mayuscula
    2: nombre.lower(),#Convierte todo a minuscula
    3: nombre.capitalize(),#Convierte solo la primer letra en mayuscula.

}

#Comparo la opción elejida por el usuario por las opciones dentro del diccionario para realizar la conversión necesaria.
if ultimo_caracter in opciones:
    print(opciones[ultimo_caracter])
   
else:
    print("ingrese su nombre con una opción correcta")  

 #Ejercicio9
magnitud_terremoto=int(input("Ingrese la magnitud del terremoto en números."))

if magnitud_terremoto<3:
    print ("Muy leve")
elif magnitud_terremoto>=3 and magnitud_terremoto<4:
    print("Leve")
elif magnitud_terremoto>=4 and magnitud_terremoto<5:
    print("Moderado")
elif magnitud_terremoto>=5 and magnitud_terremoto<6:
    print("Fuerte")
elif magnitud_terremoto>=6 and magnitud_terremoto<7:
    print("Muy fuerte")
else:
    print ("Extremo")


#Ejercicio10

hemisferio=input("En que hemisferio se encuentra? (N/S) ")
#Utilizo .Upper para que si el usuario ingresa la letra en minuscula Siempre la convierta en Mayuscula. 
hemisferio=hemisferio.upper()

mes=input("ingrese en que mes se encuentra ")
#Convierto la primer letra de la palabra en Mayuscula.
mes=mes.capitalize()
print(mes)

dia=int(input("ingrese la fecha "))

#Creo el Primer IF para identificar en que hemisferio nos encontramos, según eso hay un diccionario con cada mes que indica a cada estación.
if hemisferio == "N":
    estaciones={
        'Invierno':["Diciembre","Enero","Febrero","Marzo"],

        'Primavera':["Abril","Mayo"],

        'Verano':["Junio","Julio","Agosto","Septiembre"],

        'Otoño':["Octubre","Noviembre"],

    }
    #Este If busca si el mes ingresado se encuentra dentro del indice Verano, de ser así compara las fechas. si es menor al 21 de Junio estamos en primavera pero si es mayor al 21 de Septiembre es Otoño. 
    if mes in estaciones["Verano"]:
          
        if (mes== "Junio" and dia<21):
            print("Primavera")   
        elif (mes== "Septiembre" and dia>21):
            print("Otoño")    
        else: 
            print ("Verano")

    if mes in estaciones["Otoño"]:
        if (mes == "Septiembre" and dia>=21) or (mes=="Diciembre" and dia<21):
            print("Otoño")

    #Hace lo mismo que con verano pero con el mes de invierno
    if mes in estaciones["Invierno"]:

        if (mes== "Diciembre" and dia<21):
            print("Otoño")   
        elif (mes== "Marzo" and dia>21):
            print("Primavera")    
        else: 
            print ("Invierno")
        
    if mes in estaciones["Primavera"]:
        if (mes== "Marzo" and dia>=21) or (mes=="Junio" and dia<21):
            print("Primavera")
    
#Repite lo mismo que en el Hemisferio Norte nada mas que teniendo en cuenta las estaciones según los meses en el Hemisferio Sur. 

if hemisferio == "S":
    estaciones={
        'Verano':["Diciembre","Enero","Febrero","Marzo"],

        'Otoño':["Abril","Mayo"],

        'Invierno':["Junio","Julio","Agosto","Septiembre"],

        'Primavera':["Octubre","Noviembre"],

    }
    
    if mes in estaciones["Invierno"]:
          
        if (mes== "Junio" and dia<21):
            print("Otoño")   
        elif (mes== "Septiembre" and dia>21):
            print("Primavera")    
        else: 
            print ("Invierno")

    if mes in estaciones["Primavera"]:
        if (mes == "Septiembre" and dia>=21) or (mes=="Diciembre" and dia<21):
            print("Primavera")

    if mes in estaciones["Verano"]:

        if (mes== "Diciembre" and dia<21):
            print("Primavera")   
        elif (mes== "Marzo" and dia>21):
            print("Otoño")    
        else: 
            print ("Verano")
        
    if mes in estaciones["Otoño"]:
        if (mes== "Marzo" and dia>=21) or (mes=="Junio" and dia<21):
            print("Otoño")



