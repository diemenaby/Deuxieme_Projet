#importer le module « random ».
import random
#la fonction 'random.randint()' pour générer un entier aléatoire compris entre 1 et 100.
NombreAleatoire=random.randint(1,100)
# la fonction « input » pour demander au joueur de saisir sa supposition sous forme de chaîne.
NombreSaisie = input("Donner un nombre compris entre 1 et 100 :")
#la fonction « int » pour convertir la supposition du joueur en un entier.
NombreSaisie = int(NombreSaisie)
while NombreAleatoire != NombreSaisie :
    if NombreSaisie < NombreAleatoire:
        print("La valeur saisie est inferieure")
        NombreSaisie = int(input("Donner un nombre compris entre 1 et 100 :"))
    elif NombreSaisie > NombreAleatoire:
        print("la valeur saisie est trops elevee")
        NombreSaisie = int(input("Donner un nombre compris entre 1 et 100 :"))
print("Felicitation Vous venez de trouver le nombre qui est :", NombreSaisie)
