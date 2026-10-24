a = float(input("Introduce el valor de A: "))
b = float(input("Introduce el valor de B: "))

print(f'Antes del intercambio: A = {a:.2f}, B = {b:.2f}')

auxiliar = a
a = b
b = auxiliar

print(f'Después del intercambio: A = {a:.2f}, B = {b:.2f}')
