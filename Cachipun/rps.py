import random

#Obtener opcion del usuario
user = input("0->Rock, 1->Paper, 2->Scissors: ")


#Optener opcion del computador
comp = random.randint(0,2)

#Mirar soluciones
if user == comp:
    print("User",user,"Comp", comp, "->", "TIE")

elif (user == 0 and comp == 1) or (user == 1 and comp == 2) or (user == 2 and comp == 0): 
    print("User",user,"Comp", comp, "->", "COMP WINS")

elif (user == 1 and comp == 0) or (user == 2 and comp == 1) or (user == 0 and comp == 2):
    print("User",user,"Comp", comp, "->", "USER WINS")
