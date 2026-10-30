caracter = ""

vocales = ["a", "e", "i", "o" ,"u"]

while caracter != " ":
    caracter = input("Escribe un caracter: ")
    if caracter in vocales:
        print("Es una vocal")
    elif caracter == " ":
        print("Se acabo el juego")
    else:
        print("No es una vocal")
    

