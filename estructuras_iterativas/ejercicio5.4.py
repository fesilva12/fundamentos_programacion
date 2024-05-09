numero = int(input("Ingrese un número de 5 dígitos: "))
suma = 0


#El ciclo te permite trabajar entre 10000 y 99999
while numero <= 10000 and numero >= 99999:
    print("elija un número de 5 dígitos")
    numero = int(input("Ingrese un número de 5 dígitos: "))
for i in range(4):
    if numero % 10 == 0:
        suma += 1
    numero /= 10
    numero = int(numero)
print(f"El número tiene {suma} ceros.")

