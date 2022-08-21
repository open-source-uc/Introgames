import gato

print("EMPIEZA EL JUEGO")

j = 1 #De que jugador es el turno
continuar = True

while continuar:
    
    #Imprimir el tablero actual
    t = gato.tablero_imprimible()
    print(t)

    #Pedir Tirada
    print("Turno Jugador",j)
    f = int(input("Fila? ")) + 1
    c = int(input("Columna? ")) + 1

    #Hacer tirada
    libre = gato.esta_libre(f,c)
    if libre:
        gato.poner_ficha(f,c,j)
    else:
        print("Casilla Ocupada! Persiste el turno")

    #Comprobar ganador, empate, o continuar
    g = gato.ganador()

    if g == 1:
        print("Ganaste Jugador 1")
        continuar = False

    elif g == 2:
        print("Ganaste Jugador 2")
        continuar = False

    else:
        ocupado = gato.ocupado()

        if ocupado:
            print("Empate")
            continuar = False

        else:
            #Cambiar el turno
            if j == 1:
                j = 2
            else:
                j = 1

t = gato.tablero_imprimible
print(t)       
print("ACABA EL JUEGO")

