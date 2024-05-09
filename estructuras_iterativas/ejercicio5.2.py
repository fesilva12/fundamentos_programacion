from os import system
system('clear')

suma = 0

for i in range(3):
    print(f"Alumno {i+1}")
    nota1 = float(input("Ingrese nota: "))
    nota2 = float(input("Ingrese nota: "))
    prom = (nota1+nota2)/2
    print(f"Su promedio es: {prom}")
    suma += prom #Realizará una suma de todos los promedios.

prom_total = suma/3
print(f"El promedio del curso es: {prom_total:.1f}")