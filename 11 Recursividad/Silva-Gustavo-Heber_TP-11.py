#Ejercicio1
def rango_numeros(n):
    lista=[]
    for i in range (n,0,-1):
        lista.append (factorial(i))
    return f'{lista[]}, '

def factorial(n):
    if n==0:
        return 1
    else:
        return factorial(n-1)*n

num=int(input("Ingrese un número entero "))

print (rango_numeros(num))

#Ejercicio2
from herramientas import enteros_positivos

def fibonacci(n):
   
    if n==0 or n == 1:
        return n
    else:
        
        return fibonacci(n-1) + fibonacci(n-2)
def fibonacci_lista(n):
    if n==0:
        return [0]
    elif n==1:
        return[0,1]
    else:
        lista_fib=fibonacci_lista(n-1)
        siguiente_fib=lista_fib[-1]+lista_fib[n-2]
        lista_fib.append(siguiente_fib)
        return lista_fib
 
    

lista=[]
n=enteros_positivos('Ingrese la posicion que desea conocer de la serie de Fibonacci',0)
print(fibonacci(n))
print(fibonacci_lista(n)[0:n+1])

#Ejercicio4
def binario_recursivo(n):
    if n==1:
        return '1'
    elif n==0:
        return '0'
       
    else:
        return binario_recursivo(n//2) +str(n%2)
        
from herramientas import enteros_positivos

num=enteros_positivos("Ingrese un numero para convertirlo en binario ",1)
print(f'El numero {num} es {binario_recursivo(num)} en binario')

#Ejercicio6
from herramientas import enteros_positivos

def suma_digitos(n):
    if (n//10)==0:
        return n%10
    else:
        l=suma_digitos(n//10)+suma_digitos(n%10)
        return l
    



num=enteros_positivos('Ingrese un número positivo',0)
print (suma_digitos(num))

#Ejercicio7
from herramientas import enteros_positivos

def contar_bloques(n):
    l=0
    if n==1:
        return 1
    else:
        l= contar_bloques(n-1)+n
        return l

bloques_base=enteros_positivos("Ingrese el numero de bloques en la primer fila ",0)
print(f'Se necesitan {contar_bloques(bloques_base)} para armar la piramide')

#Ejercicio8

from herramientas import enteros_positivos

def contar_digito(n,m):
    
    if n//10==0 and n%10!=m:
        return 0
    elif n//10 ==0 and n%10==m:
        return 1
    else:
        l=contar_digito(n//10,m)+((n%10)==m)
    return l

num=enteros_positivos("Ingrese un numero entero positivo ",0)
num_buscado=enteros_positivos("Ingrese el digito que desea buscar ", 0,9)
print(contar_digito(num,num_buscado))

