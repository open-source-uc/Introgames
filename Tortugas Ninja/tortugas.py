import random

#Numero al azar del computador
num = random.randint(1,100)

limite = int(input("Numero de intentos: "))

encontrado = False
intento = 0

while not encontrado:
    print("Intento", intento)
    n = int(input("=> "))

    if n < num:
        print("Demasiado pequeno")
        intento += 1
    elif n > num:
        print("Demasiado grande")
        intento += 1
    else:
        print("CORRECTO")
        encontrado = True

#El while acaba por que lo encontraste
# o quedaste sin intentos
if encontrado:
    print("FELICIDADES GANASTE")
elif intento == limite:
    print("Te quedaste sin intentos! :(")
    print("El numero era", num)
    
