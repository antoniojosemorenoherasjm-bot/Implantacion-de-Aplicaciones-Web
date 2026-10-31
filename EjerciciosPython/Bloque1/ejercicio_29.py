base = float(input("Introduce la base: "))
expo = int(input("Introduce el exponente: "))

resultado = 1
for x in range(expo):
    resultado = resultado * base

print(f'La potencia de {base} elevado a {expo} es igual a {resultado}')