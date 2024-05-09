cantidad = int(input("Ingrese cantidad de números que quiere agregar: "))
prom = 0

for i in range(cantidad):
    numero = int(input("Ingrese número entero: "))
    prom += numero
    print(numero)
    print(prom)

promedio = prom/cantidad
print(f"{promedio:.1f}")