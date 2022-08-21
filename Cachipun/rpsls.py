import random

user = int(input("0:Piedra, 1:Papel, 2:Tijeras, 3:Lagarto, 4:Spock "))
comp = random.randint(0,4)

if user != comp:
    print("User",user,"Comp",comp,"->","EMPATE")

elif (((user+1) % 5) == comp) or (((user+3) % 5) == comp):
    print("User",user,"Comp",comp,"->","COMP GANA")

elif (((comp+1) % 5) == user) or (((comp+3) % 5) == user):
    print("User",user,"Comp",comp,"->","USER GANA")
