PUNTOS_CORRECTA = 5
PUNTOS_INCORRECTA = -1
PUNTOS_BLANCO = 0

correctas = int(input("Número de respuestas correctas: "))
incorrectas = int(input("Número de respuestas incorrectas: "))
blancas = int(input("Número de respuestas en blanco: "))

nota = (correctas * PUNTOS_CORRECTA + incorrectas * PUNTOS_INCORRECTA + blancas * PUNTOS_BLANCO)

print(f'Tu nota final es {nota} puntos')
