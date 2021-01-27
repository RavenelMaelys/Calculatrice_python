#On demande a l'utilisateur de rentrer une opération simple.
nombre1=int(input('Entrer le premier nombre: '))
signe=str(input('Entrer le signe du calcul: '))
nombre2=int(input('Entrer le deuxieme nombre: '))

# addition
if (signe == "+"):
    resultat = nombre1+nombre2
# soustraction
elif (signe == "-"):
    resultat = nombre1-nombre2

# multiplication
elif (signe == "*"):
    resultat = nombre1* nombre2
 # divsion
elif (signe == "/"):
    resultat = nombre1/nombre2
else:
    print("Signe invalide")

print("Le resultat est: ", resultat)
