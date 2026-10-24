# Valor de cada moneda en céntimos
MONEDA_2_EUROS = 200
MONEDA_1_EUROS = 100
MONEDA_50_CENT = 50
MONEDA_20_CENT = 20
MONEDA_10_CENT = 10

monedas_2 = int(input("Monedas de 2 €: "))
monedas_1 = int(input("Monedas de 1 €: "))
monedas_50 = int(input("Monedas de 50 céntimos: "))
monedas_20 = int(input("Monedas de 20 céntimos: "))
monedas_10 = int(input("Monedas de 10 céntimos: "))

total_centimos = (monedas_2 * MONEDA_2_EUROS) + (monedas_1 * MONEDA_1_EUROS) + (monedas_50 * MONEDA_50_CENT) + (monedas_20 * MONEDA_20_CENT) + (monedas_10 * MONEDA_10_CENT)

euros = total_centimos // 100
centimos = total_centimos % 100

print(f'Tienes {euros} euros y {centimos} céntimos')
