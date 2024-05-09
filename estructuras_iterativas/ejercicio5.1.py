#While True repite el ciclo hasta que sucede algo
while True:
    a = int(input("Ingrese A: "))
    b = int(input("Ingrese B: "))   
    if a<b:
        for i in range(a,b+1):
            print(i)
        break
    else:
        print("mal ahí mi loco")