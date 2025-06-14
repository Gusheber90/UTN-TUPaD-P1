#Ejercicio1
def precios_frutas():#Esta funcion guarda el diccionario original para poder reutilizarlo en otros ejercicios  
    precios_frutas={'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
    return precios_frutas

precios_nuevas_frutas=precios_frutas()
print(precios_nuevas_frutas)
for i in range (0,3):#Utilizo un bucle for que permite agregar 3 keys con su valor para agregar 3 nuevas frutas con sus respectivos precios
   f=input('Ingrese fruta ')
   v=int(input('Ingrese valor de la fruta '))
   precios_nuevas_frutas[f]=v

print(precios_nuevas_frutas)

#Ejercicio2
actualizacion_frutas=precios_nuevas_frutas
frutas_a_modificar=['Banana', 'Melón', 'Manzana']
for frutas in frutas_a_modificar:
    if frutas in nuevos_precios:
        precio_nuevo=int(input(f'Ingrese el nuevo precio para {frutas_a_cambiar} '))
        nuevos_precios[frutas_a_cambiar]=precio_nuevo
print(nuevos_precios)


#Ejercicio3
lista_frutas=precios_frutas()
frutas = list(lista_frutas.keys())
print(frutas)

#Ejercicio4

# Diccionario vacio para almacenar datos.
agenda = {}

print("CARGA DE CONTACTOS:")
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto #{i+1}: ")
    numero = input(f"Ingresá el numero telefonico de {nombre}: ")
    agenda[nombre] = numero

# # Consultar un contacto
print("\nCONSULTA DE NUMERO TELEFONICO:")
nombre_buscado = input("Ingresa el nombre del contacto a buscar: ")

if nombre_buscado in agenda:
    print(f"El numero de {nombre_buscado} es {agenda[nombre_buscado]}")
else:
    print(f"No se encontro ningun contacto con el nombre '{nombre_buscado}'.")

#Ejercicio5

frase = input("Ingresa una frase")

palabras = frase.lower().split()

# Obtener palabras unicas
palabras_unicas = set(palabras)
print("\nPalabras únicas:")
print(palabras_unicas)

 # Contar cantidad de veces que aparece cada palabra
contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1


print("\nCantidad de apariciones de cada palabra:")
for palabra, cantidad in contador_palabras.items(): # Permite recorrer dentro del bucle for items del diccionario y mostrarlos en print
    print(f"{palabra}: {cantidad}")


#Ejercicio6

Diccionario vacio para guardar los alumnos y sus notas
alumnos = {}

# # Cargamos los datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    notas = []

    for j in range(3):
        nota = float(input(f"Ingresá la nota {j+1} de {nombre}: "))
        notas.append(nota)

    alumnos[nombre] = tuple(notas)  # Guardar las notas como tupla

# Calcular y mostrar el promedio de cada alumno
print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

#Ejercicio8

# Diccionario con productos y su stock inicial
stock_productos = {
    "manzanas": 10,
    "naranjas": 15,
    "bananas": 5
}

# Menu principal
while True:
    print("\n--- MENU DE STOCK ---")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades a un producto existente")
    print("3. Agregar un producto nuevo")
    print("4. Ver todos los productos y su stock")
    print("5. Salir")
    
    opcion = input("Elegir una opcion (1-5): ")
    
    if opcion == "1":
        producto = input("Ingresar nombre del producto: ").lower()
        if producto in stock_productos:
            print(f"Stock de {producto}: {stock_productos[producto]} unidades")
        else:
            print("El producto no existe en el sistema.")
    
    elif opcion == "2":
        producto = input("Producto al que queres agregar unidades: ").lower()
        if producto in stock_productos:
            agregar = int(input("Cuantas unidades queres agregar?: "))
            stock_productos[producto] += agregar
            print(f"Nuevo stock de {producto}: {stock_productos[producto]} unidades")
        else:
            print("El producto no existe. Primero agregalo como nuevo.")
    
    elif opcion == "3":
        producto = input("Nombre del nuevo producto: ").lower()
        if producto in stock_productos:
            print("Ese producto ya existe.")
        else:
            nuevo_stock = int(input("Stock inicial del nuevo producto: "))
            stock_productos[producto] = nuevo_stock
            print(f"{producto} agregado con {nuevo_stock} unidades de stock.")

    elif opcion == "4":
        print("\n--- LISTA DE PRODUCTOS ---")
        for prod, stock in stock_productos.items():
            print(f"{prod}: {stock} unidades")
    
    elif opcion == "5":
        print("Saliendo del sistema...")
        break
    
    else:
        print("Opcion invalida. Elegi una del 1 al 5.")

#Ejercicio9

agenda = {
("lunes", "10:00"): "Reunion con equipo",
("martes", "14:00"): "Clase de ingles",
("viernes", "18:30"): "Gimnasio"
}

# Pido al usuario que ingrese el dia y la hora
dia = input("Ingresar dia (ej: lunes): ").lower()
hora = input("Ingresar hora (ej: 10:00): ")

# Armo la tupla con el dia y la hora ingresados
clave = (dia, hora)

 # Consulto si existe un evento en ese dia y hora
if clave in agenda:
    print(f"Actividad programada: {agenda[clave]}")
else:
    print("No hay actividades en ese dia y hora.")

#Ejercicio10

def invertir_diccionario(diccionario_original):
    return {capital: pais for pais, capital in diccionario_original.items()}

 # Diccionario de ejemplo (puedes reemplazarlo con uno más grande)
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Francia": "Paris",
    "Japon": "Tokio",
    "Alemania": "Berlin",
    "Italia": "Roma",
    "España": "Madrid"
}

capitales_paises = invertir_diccionario(paises_capitales)

print("Diccionario original:")
print(paises_capitales)

print("\nDiccionario invertido:")
print(capitales_paises)