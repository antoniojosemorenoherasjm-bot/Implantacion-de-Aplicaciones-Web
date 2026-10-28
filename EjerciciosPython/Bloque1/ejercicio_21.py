numero = int(input("Introduce un número: "))

resultado = 1

numero_factorial = 1

while numero_factorial <= numero:
    resultado = resultado * numero_factorial
    numero_factorial = numero_factorial +1

print(f'El factorial de {numero} es igual a {resultado}')