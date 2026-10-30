suma = 0 
cantidad = 0
numero = 1

while numero != 0:
    numero = int(input("Introduce tu número: "))
    suma = suma + numero
    cantidad = cantidad + 1

print(f'La suma de todos los números introducidos es {suma:.2f}')

if (cantidad - 1) == 0:
    print("No se puede dividir, no has introducido ningún número")
else: 
    media = suma / (cantidad - 1)
    print(f'La media de los números introducidos es {media:.2f}')