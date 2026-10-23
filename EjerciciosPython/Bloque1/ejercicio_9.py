DESCUENTO = 0.15

total_compra = float(input("Introduce el total de su compra: "))

ahorro = DESCUENTO * total_compra 

compra_con_descuento = total_compra - (ahorro)

print(f'Con una compra de {total_compra:.2f} euros, aplicando el descuento del 15% usted se ahorrará {ahorro:.2f} euros y pagará un total de {compra_con_descuento:.2f} euros')
