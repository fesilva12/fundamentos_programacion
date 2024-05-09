num = 1
sum = 0
sum1 = 0
numero = -999999
while num != 0:
    num = int(input("Ingrese un dígito: "))
    if num % 2 ==0:
        sum += 1
    elif num % 2 != 0:
        sum1 += 1
    if num >= numero:
        numero = num
    else:
        continue
print(f"la cantidad de pares es: {sum-1}") 
#sum-1 porque el cero lo considera par python
print(f"la cantidad de impares es: {sum1}")
print(f"El mayor dígito ingresado es: {numero}")