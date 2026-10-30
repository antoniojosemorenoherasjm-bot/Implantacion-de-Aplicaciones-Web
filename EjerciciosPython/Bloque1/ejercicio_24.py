cantidad = int(input("¿Cuántos números vas a introducir? ->"))

positivos = 0
negativos = 0
igual_cero = 0

for x in range(cantidad):
    numero = int(input("Introduce tu número: "))
    if numero > 0:
        positivos = positivos + 1
    elif numero < 0:
        negativos = negativos + 1
    elif numero == 0:
        igual_cero = igual_cero + 1

print(f'Has introducido {positivos} números positivos')
print(f'Has introducido {negativos} números negativos')
print(f'Has introducido {igual_cero} números iguales a cero')