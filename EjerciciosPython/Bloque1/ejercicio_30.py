numeros = [1, 2, 3, 4, 5]
multiplicadores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for tabla in (numeros):
    for multiplicador in (multiplicadores):
        resultado = tabla * multiplicador
        print(f'{tabla} x {multiplicador} = {resultado}')