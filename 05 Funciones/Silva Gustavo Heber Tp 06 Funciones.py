#Ejercicio1
def hola_mundo():
    return "Hola mundo!"

print(hola_mundo())

#Ejercicio2
def saludar_ususario(nombre):
    return f"Hola {nombre}!"

print(saludar_ususario("Gustavo"))


#Ejercicio 3

def informacion_personal(nombre,apellido,edad,residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

nombre=input("Nombre: ").capitalize()
apellido=input("Apellido: ").capitalize()
edad=input("Edad: ")
residencia=input("Residencia: ").capitalize()

print(informacion_personal(nombre,apellido,edad,residencia))

#Ejercicio 4
def calcular_area_circulo(radio):
    area= 3.14159*radio**2
    return f"El area del circulo es {area}"

def calcular_perimetro_circulo(radio):
    perimetro=2*3.14159*radio
    return f"El perímetro del circulo es {perimetro}"

radio=int(input("Por favor ingrese el radio del circulo "))
print(calcular_area_circulo(radio),calcular_perimetro_circulo(radio))


#Ejercicio 5
def segundos_horas(segundos):
    horas=segundos/3600
    return f'estos {segundos} segundos equivalen a {horas} horas'

segundos=int(input("Ingrese la cantidad de segundos "))
print (segundos_horas(segundos))


#Ejercicio 6

def tabla_multiplicar(numero):
    resultado=[]
    for i in range (1,11):
        multiplo=numero*i
        resultado.append(f'{numero} x {i} = {multiplo}')
    return'\n'.join(resultado)

numero=int(input('Ingrese un número '))
print(tabla_multiplicar(numero))

#Ejercicio 7

def operaciones_basicas(a,b):
    suma=f'la suma de a+b es {a+b}'
    resta=f'la resta de a-b es {a-b}'
    multiplicacion=f'la multiplicacion de a*b es {a*b}'
    division=f'la division de a/b es {a/b}'
    tupla=(suma,resta,multiplicacion,division)
    return '\n'.join(tupla)

a=int(input('Ingrese el valor de a '))
b=int(input('Ingrese el valor de b '))
print(operaciones_basicas(a,b))

#Ejercicio 8

def calcular_imc(peso,atura):
    imc=peso/altura**2
    imc=int(imc*100)/100
    return f'El IMC segun los valores ingresados es de {imc}'

peso=int(input('Ingrese el peso '))
altura=float(input('Ingrese la estatura '))

print(calcular_imc(peso,altura))

#Ejercicio 9

def celsius_fahrenheit(celsius):
    fahr=celsius*9/5 +32
    return f'los {celsius} grados celsius equivalen a {fahr} grados fahrenheit'

celsius=int(input('Ingrese la temperatura en grados centigrados '))
print(celsius_fahrenheit(celsius))

#Ejercicio 10

def calcular_promedio(a,b,c):
    promedio=(a+b+c)/3
    promedio=int(promedio*100)/100
    return f'El promedio de sumar a+b+c es {promedio}'

a=int(input ('Ingrese el valor de a '))
b=int(input ('Ingrese el valor de b '))
c=int(input ('Ingrese el valor de c '))
print(calcular_promedio(a,b,c))
