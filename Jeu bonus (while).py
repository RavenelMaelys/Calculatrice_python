objectif = 6 #on peut changer le nombre a deviner dans le programme
trouve = False
essai=0
while (trouve == False):
    choix = int(input("entrer un nombre: "))
    essai=essai+1
    if (choix < objectif):
        print("Le nombre est plus grand!")
    elif (choix > objectif):
        print("Le nombre est plus petit!")
    
    else:
        print("Bravo, tu as trouvé le bon nombre. C'était: ",objectif)
        print("Tu l'as trouvé en ", essai, "essais !")
        trouve = True
