opcion = int(input("""1. Cuadrado
2. Rectángulo
3. Triángulo
4. Círculo
5. Salir
Ingrese opción: """))

while opcion != 5:
    if opcion == 1:
        lado = int(input("Ingrese lado: "))
        print(f"El área del cuadrado es: {lado * lado}")
    elif opcion == 2:
        ancho = int(input("Ingrese ancho: "))
        largo = int(input("Ingrese largo: "))
        print(f"El área del rectángulo es: {ancho*largo}")
    elif opcion == 3:
        base = int(input("Ingrese base: "))
        altura = int(input("Ingrese altura: "))
        print(f"El área del triángulo es: {(base*altura)/2}")
    elif opcion == 4:
        radio = int(input("Ingrese radio: "))
        print(f"El área del circulo es: {3.14 *(radio**2)}")
    else:
        print("Número incorrecto")
    opcion = int(input("Ingrese opcion: "))

