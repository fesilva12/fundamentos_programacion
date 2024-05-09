letra = ()
suma = 0
#El ciclo se repite hasta que el usuario ingresa salir.
while letra != "salir":
    letra = input("Ingrese letra: ")
    if len(letra) == 1:
        suma += 1
    else:
        continue
print(f"La cantidad de letras leídas es {suma}.")