suma = 0
mult = 1
num = int(input("Ingrese un número: "))

for i in range(num):
    suma +=1
    mult = mult * suma
print(f"El factorial de {num} es {mult}.")
