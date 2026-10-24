x1 = float(input("Coordenada x del primer punto: "))
y1 = float(input("Coordenada y del primer punto: "))
x2 = float(input("Coordenada x del segundo punto: "))
y2 = float(input("Coordenada y del segundo punto: "))

distancia = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5

print(f'La distancia entre ({x1:.2f}, {y1:.2f}) y ({x2:.2f}, {y2:.2f}) es {distancia:.2f}')
