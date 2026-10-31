inferior = int(input("Introduce el límite inferior: "))
superior = int(input("Introduce el límite superior: "))

while inferior > superior:
    print(f'No tiene sentido que el inferior sea mayor que el superior, vuelve a introducirlos')
    inferior = int(input("Introduce el límite inferior: "))
    superior = int(input("Introduce el límite superior: "))

fuera = 0
igual = 0 
suma = 0
numero = 1

while numero != 0:
    numero = int(input("Introduce un número: "))
    if numero != 0:
        if inferior < numero < superior:
            suma = suma + numero
        elif numero > superior or numero < inferior:
            fuera = fuera + 1
        else:
            igual = igual + 1

print(f'La suma de los números que están dentro del intervalo es {suma}')
print(f'Has introducido {fuera} números que están fuera del intervalo')
print(f'Has introducido {igual} números que es igual al límite del intervalo')