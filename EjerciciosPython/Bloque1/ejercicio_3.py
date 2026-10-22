cateto1 = float(input("Medida del cateto 1 en metros: "))
cateto2 = float(input("Medida del cateto 2 en metros: "))

hipotenusa = (cateto1**2 + cateto2**2) ** 0.5

print(f'Con catetos de {cateto1} y {cateto2} metros, la hipotenusa mide {hipotenusa:.2f} metros')
