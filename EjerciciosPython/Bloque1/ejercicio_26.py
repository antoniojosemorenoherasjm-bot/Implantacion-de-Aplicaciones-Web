numero_mayor = int(input("Introduce tu primer número mayor: "))
numero_menor = int(input("Introduce tu segundo número menor: "))

for x in range(numero_menor, (numero_mayor + 1)): # Uso el +1 para que incluya los extremos, no se pide pero no esta mal ponerlo
    if x % 2 == 0:
        print(f'El número {x} es par y está entre los dos números dados')