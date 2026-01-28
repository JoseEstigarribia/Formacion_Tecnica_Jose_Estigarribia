def ingresar_numeros():
    numeros = []

    while True:
        entrada = input("Ingrese un número (o escriba 'salir'): ")

        if entrada.lower() == "salir":
            break

        try:
            numero = int(entrada)
            numeros.append(numero)
            print("Número agregado correctamente.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")

    return numeros


def mostrar_resumen(numeros):
    if len(numeros) == 0:
        print("No se ingresaron números.")
        return

    suma = sum(numeros)
    promedio = suma / len(numeros)

    print("\nResumen final")
    print("Cantidad de números:", len(numeros))
    print("Suma total:", suma)
    print("Promedio:", promedio)


def main():
    numeros = ingresar_numeros()
    mostrar_resumen(numeros)
    print("Números ingresados:", numeros)
    print("Programa finalizado.")


main()
