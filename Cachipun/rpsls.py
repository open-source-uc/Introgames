import random

user = int(input("0:Piedra, 1:Papel, 2:Tijeras, 3:Lagarto, 4:Spock "))
comp = random.randint(0,4)

while user != 0 and user != 1 and user != 2 and user != 3 and user != 4:
    print("Please follow the input format, select a number to play!")
    user = int(input("0:Piedra, 1:Papel, 2:Tijeras, 3:Lagarto, 4:Spock "))

if user == comp:
    print("User",user,"Comp",comp,"->","EMPATE")

elif (((user+1) % 5) == comp) or (((user+3) % 5) == comp):
    print("User",user,"Comp",comp,"->","COMP GANA")

elif (((comp+1) % 5) == user) or (((comp+3) % 5) == user):
    print("User",user,"Comp",comp,"->","USER GANA")
