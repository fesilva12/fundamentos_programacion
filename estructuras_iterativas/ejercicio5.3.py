numero = int(input("Ingrese número de vocales: "))
vocal_a = 0
vocal_e = 0
vocal_i = 0
vocal_o = 0
vocal_u = 0

for i in range(numero):
    vocal = input("Escriba una vocal: ").lower() #lower() escrie las mayusculas en minusculas.
    if vocal == "a":
        vocal_a += 1
    elif vocal == "e":
        vocal_e += 1
    elif vocal == "i":
        vocal_i += 1
    elif vocal == "o":
        vocal_o += 1
    elif vocal == "u":
        vocal_u += 1

print(f"Cantidad A:{vocal_a} E:{vocal_e} I:{vocal_i} O:{vocal_o} U:{vocal_u}")