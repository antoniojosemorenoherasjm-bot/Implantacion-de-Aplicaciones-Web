inferior = int(input("Introduce el límite inferior: "))
superior = int(input("Introduce el límite superior: "))

while inferior > superior:
    print(f'No tiene sentido que el inferior sea mayor que el superior, vuelve a introducirlos')
    inferior = int(input("Introduce el límite inferior: "))
    superior = int(input("Introduce el límite superior: "))
