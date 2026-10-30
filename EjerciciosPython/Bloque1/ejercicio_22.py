import random

numero_aleatorio = random.randint(1, 100)

intentos = 10

numero = 0 

while numero != numero_aleatorio and intentos != 0:
    numero = int(input("Introduce el número que crees que es: "))
    intentos = intentos - 1
    if numero > numero_aleatorio:
        print("El número que has introducido es demasiado grande")
        print(f'Te quedan {intentos} intentos')
    elif numero < numero_aleatorio:
        print("El número que has introducido es muy pequeño")
        print(f'Te quedan {intentos} intentos')

if numero == numero_aleatorio:
    print(f'Has acertado, el número secreto era el {numero_aleatorio} en {10 - intentos} intentos')
else:
    print(f'Se te han acabado los intentos, el número secreto era {numero_aleatorio}')