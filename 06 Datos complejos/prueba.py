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
