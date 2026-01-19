#SE aplica int al input ya que input devuelve un string
numero = int(input("Ingresa un numero"))

if numero % 2 == 0 :
    print("Numero es Par", numero)
else:
    print("El numero es impar", numero)