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
frutas = list(precios_frutas.keys())
print(frutas)
