import random

numero_secreto = random.randint(1, 25)
intentos = 0

while True:
    print("adivina el numero entre 1 y 25:")
    
    intento = float(input("ingresa tu numero :"))
    
    if intento > numero_secreto:
        print("el numero es muy alto")
        intentos += 1
    elif intento < numero_secreto:
        print("el numero es muy bajo")
        intentos += 1
    else:
        print("felicidades! has adivinado el numero")
        print(f"lo lograste en {intentos} intentos")
        break
    

    
    
