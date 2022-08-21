t = [[0,0,0],
     [0,0,0],
     [0,0,0]]

# No recibe nada
# Retorna str con el tablero listo para hacer print
def tablero_imprimible():
    txt = "\n"
    txt += n2f(t[0][0])+"|"+n2f(t[0][1])+"|"+n2f(t[0][2])+"\n"
    txt += "-+-+-\n"
    txt += n2f(t[1][0])+"|"+n2f(t[1][1])+"|"+n2f(t[1][2])+"\n"
    txt += "-+-+-\n"
    txt += n2f(t[2][0])+"|"+n2f(t[2][1])+"|"+n2f(t[2][2])+"\n"
    return txt

def n2f(n):
    if n == 1:
        res = "\u2690"
    elif n == 2:
        res = "\u2691"
    else:
        res = " "
    return res

#Recibe 2 ints: fila y columna
#Retorna bool si la celda esta libre
def esta_libre(f, c):
    libre =  t[f][c] == 0
    return libre

#Recibe 3 ints: fila, columna, y jugador (1 o 2)
#Pone la ficha del jugador en la celda
def poner_ficha(f, c, j):
    t[f][c] = j

#No Recibe nada
#Retorna bool si todo el tablero esta lleno
def ocupado():
    ocupado = ((not 0 in t[0]) and
               (not 0 in t[1]) and
               (not 0 in t[2]))
    return ocupado

#No recibe nada
#Retorna int con el ganador:
# 1 (Jug.1), 2(Jug.2), 0 (Aun no hay ganador)
def ganador():
    gana_1 = (tiene_fila(0,1) or
              tiene_fila(1,1) or
              tiene_fila(2,1) or
              tiene_columna(0,1) or
              tiene_columna(1,1) or
              tiene_columna(2,1) or
              tiene_diagonal(1))

    gana_2 = (tiene_fila(0,2) or
              tiene_fila(1,2) or
              tiene_fila(2,2) or
              tiene_columna(0,2) or
              tiene_columna(1,2) or
              tiene_columna(2,2) or
              tiene_diagonal(2))

    if gana_1:
        return 1
    elif gana_2:
        return 2
    else:
        return 0


def tiene_fila(f,j):
    tiene = ((t[f][0] == j) and
             (t[f][1] == j) and
             (t[f][2] == j))
    return tiene

def tiene_columna(c, j):
    tiene = ((t[0][c] == j) and
             (t[1][c] == j) and
             (t[2][c] == j))
    return tiene

def tiene_diagonal(j):
    tiene_diagonal = ((t[0][0] == j) and
                      (t[1][1] == j) and
                      (t[2][2] == j))
    tiene_antidiagonal = ((t[0][2] == j) and
                          (t[1][1] == j) and
                          (t[2][0] == j))
    tiene = tiene_diagonal or tiene_antidiagonal
    return tiene
    

# Si el usuario ejecuta directamente este archivo, avisarle que
# debe abrir wargames.py
if __name__ == "__main__":
    print("Para jugar al Gato, debes ejecutar wargames.py!")
    print("python3 wargames.py")
