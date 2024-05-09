num = int(input("Ingrese número: "))

for i in range(1,10):
    if i == 1 or i == num:
        continue
    elif num % i == 0:
        print("No es número primo")
        break
    else:
        print("Es número primo")
        break