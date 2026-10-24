COMISION = 0.1

sueldo = float(input("Escribe tu sueldo mensual aquí: "))
venta1 = float(input("Importe de tu primera venta: "))
venta2 = float(input("Importe de tu segunda venta: "))
venta3 = float(input("Importe de tu tercera venta: "))

total_comisiones = COMISION * (venta1 + venta2 + venta3)
sueldo_total = sueldo + total_comisiones

print(f'Con un sueldo de {sueldo:.2f} euros, tú recibirás {total_comisiones:.2f} euros en comisiones y tu sueldo total será {sueldo_total:.2f} euros')

