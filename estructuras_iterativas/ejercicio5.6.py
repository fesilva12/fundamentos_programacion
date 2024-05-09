numero = -9999999

for i in range(20):
    num = int(input("Ingrese un número: "))
    if num >= numero:
        numero = num
    else:
        continue

print(f"El mayor número es: {numero}")