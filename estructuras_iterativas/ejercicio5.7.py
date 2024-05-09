cantidad = int(input("Ingrese cuantos números enteros desea sumar: "))
suma = 0
suma2 = 0

for i in range(cantidad):
    suma += 1
    suma2 = suma + suma2
print(f"La suma de los {cantidad} primeros números enteros es: {suma2}")