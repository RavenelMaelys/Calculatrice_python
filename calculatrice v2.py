#on définit a l'aide de la fonction "def" une fonction.
def addition (num1, num2):
    print(num1,"+",num2,"=",num1+num2)

def soustraction (num1, num2):
    print(num1,"-",num2,"=",num1-num2)

def multiplication (num1, num2):
    print(num1,"*",num2,"=",num1*num2)
    
def division (num1, num2):
    if (num2==0):
        print("division impossible")
    else:
        print(num1,"/",num2,"=",num1/num2)
    
def puissance (num1, num2):
    r=1
    for k in range(0, num2):
        r=r*num1
    print(num1,"^",num2,"=",r)
#on affiche les différentes possibilitées.
print("Selectionnez l'opération voulue")
print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")
print("5. Puissance")
#while true est une boucle qui tourne indéfiniement.
#dans celle-ci, on demande à l'utilisateur quelle opération il veut effectuer,
#on fait le calcul et on l'affiche.
#Le programme va alors recommencer la boucle
#et redemander a l'utilisateur d'effectuer un calcul.
while True:
    choix= int(input("Entrer votre choix: "))
    print(choix)
    num1=int(input("Entrer un nombre: "))
    num2=int(input("Entrer un nombre: "))
    #on crée un "if" pour couvrir toutes les possibilité de la calculatrice.
    if (choix == 1):
        addition(num1,num2)
    
    elif (choix == 2):
        soustraction(num1,num2)

    elif (choix == 3):
        multiplication(num1,num2)
        
    elif (choix == 4):
        division(num1,num2)

    elif (choix == 5):
        puissance(num1,num2)
    else:
        print("Veuillez entrer une commande valide")

