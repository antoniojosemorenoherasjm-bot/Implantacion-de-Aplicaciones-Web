parcial1 = float(input("Introduce la nota de tu primer parcial: "))
parcial2 = float(input("Introduce la nota de tu segundo parcial: "))
parcial3 = float(input("Introduce la nota de tu tercer parcial: "))

examenfinal = float(input("Introduce la nota del examen final: "))
trabajofinal = float(input("Introduce la nota de tu trabajo final: "))

promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
aporte_examenfinal = examenfinal * 0.3
aporte_trabajo = trabajofinal * 0.15

nota_final = (aporte_trabajo + aporte_examenfinal + (promedio_parciales * 0.55))

print(f'Tu nota final es {nota_final:.2f}')

