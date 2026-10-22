cateto1 = int(input("Medida del cateto 1 en metros: "))
cateto2 = int(input("Medida del cateto 2 en metros: "))

hipotenusa = (cateto1*cateto1 + cateto2*cateto2) ** 0.5

print(f'Dados los dos catetos de un triángulo rectángulo su hipotenusa es {hipotenusa}')
