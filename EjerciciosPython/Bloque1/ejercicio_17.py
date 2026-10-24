horas = int(input("Hora de salida (HH): "))
minutos = int(input("Minutos de salida (MM): "))
segundos = int(input("Segundos de salida (SS): "))
duracion = int(input("Duración del viaje en segundos: "))

salida_en_segundos = (horas * 3600) + (minutos * 60) + (segundos)
llegada_en_segundos = salida_en_segundos + duracion

horas_llegada = llegada_en_segundos // 3600
resto = llegada_en_segundos % 3600
minutos_llegada = resto // 60
segundos_llegada = resto % 60

print(f'Llegará a la ciudad B a las {horas_llegada:02d}:{minutos_llegada:02d}:{segundos_llegada:02d}')
