PESO_PARCIALES = 0.55
PESO_EXAMEN = 0.3
PESO_TRABAJO = 0.15

parcial1 = float(input("Introduce la nota de tu primer parcial: "))
parcial2 = float(input("Introduce la nota de tu segundo parcial: "))
parcial3 = float(input("Introduce la nota de tu tercer parcial: "))

examen_final = float(input("Introduce la nota del examen final: "))
trabajo_final = float(input("Introduce la nota de tu trabajo final: "))

promedio_parciales = (parcial1 + parcial2 + parcial3) / 3

aporte_parciales = promedio_parciales * PESO_PARCIALES
aporte_examen = examen_final * PESO_EXAMEN
aporte_trabajo = trabajo_final * PESO_TRABAJO

nota_final = aporte_parciales + aporte_examen + aporte_trabajo

print(f'Tu nota final es {nota_final:.2f}')
