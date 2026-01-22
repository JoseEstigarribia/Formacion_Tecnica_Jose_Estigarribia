"""Se necesita un pequeño script en Python que permita:

Ingresar números por teclado

Validar que sean números enteros

Guardarlos en una lista

Permitir salir del programa

Mostrar un resumen final"""
# Uso lista para almacenar los numeros ingresados por el usuario.
numeros = []
#Bucle pide Ingresar numero, si no se cumple condicon de corte, es infinito.
while True:
    entrada = input("Ingrese un número (o escriba 'salir'): ")
    #Verifico en minusculas, la condicion de Corte.
    if entrada.lower() == "salir":
        break
    #Bloque try/except No rompe el bucle hace que continue apesar de valor invalido ingresado.
    try:
        numero = int(entrada)
        numeros.append(numero)
        print("Número agregado correctamente.")
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero.")

"""Mejora 

Al finalizar el programa, mostrar:

Cantidad de números ingresados

Suma total

Promedio"""

if len(numeros) > 0:
    suma = sum(numeros)
    promedio = suma / len(numeros)
    print("Cantidad de números:", len(numeros))
    print("Suma total:", suma)
    print("Promedio:", promedio)
else:
    print("No se ingresaron números.")

#al final muestro la lista completa
print("Programa finalizado.")
print("Números ingresados:", numeros)
