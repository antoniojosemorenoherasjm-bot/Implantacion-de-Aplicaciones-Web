distancia = float(input("Distancia entre los vehículos (km): "))
v1 = float(input("Velocidad del vehículo de detrás (km/h): "))
v2 = float(input("Velocidad del vehículo de delante (km/h): "))

velocidad_relativa = v1 - v2
tiempo_horas = distancia / velocidad_relativa
tiempo_minutos = tiempo_horas * 60

print(f'El vehículo de detrás alcanzará al otro en {tiempo_minutos:.2f} minutos')
