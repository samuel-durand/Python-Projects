#import la fonction random
import random

#Choisir dans le fichier dico un mot aléatoirement 
with open("C:\\Users\\jiyel\\Desktop\\PLATEFORME\\PYTHON\\EXO_2\\LE PENDU\\dico_france.txt", "r", encoding="UTF-8") as file:
    dico=file.read()
    mots=dico.split()

#print(random.choice(mots))

#d = open("dico_france.txt", "r") 
#y = d.read
# solution = random.choice(choix)
# solution = [random.choice(list(d)) for i in range(10)]

#Créer une condition ou le niveau choisis affiche le nombre de vie correspondant #(10, 7, 4)
# et donc crée une variable “vie” qui diminue avec le nombre d’erreur effectuer
deb = "débutant"
inter="intermédiaire"
exp="expert"

viedeb=10
vieint=7
viexp=4

solution = random.choice(mots)
#tentatives = 10
affichage = ""
lettres_trouvees = ""
liste =[]

for l in solution:
    affichage = affichage + "_ "

print(">> Bienvenue dans le pendu <<")

     #le true permet de revenir sur le choix du niveau lorsque l'on se trompe sur l'orthographe
    #faire un input qui permet au joueur de choisir son niveau : “choisis ton niveau entre #débutant, intermédiaire et expert : “
niveau=input("choisis ton niveau entre débutant, intermédiaire et expert : ")
     
if niveau == deb:
        
        while viedeb > 0:
            print("Nombre de vie(s) :",viedeb)
            print("\nMot à deviner : ", affichage)
            proposition = input("proposez une lettre : ")[0:1].lower()
            liste = liste + [proposition]
            print(liste)

            if proposition in solution:
                lettres_trouvees = lettres_trouvees + proposition
                print("-> Bien vu!")
            else:
                viedeb = viedeb - 1
                print("-> Mauvaise réponse!\n")
                if viedeb<=0:
                    print(" ==========Y= ")
                if viedeb<=1:
                    print(" ||/       |  ")
                if viedeb<=2:
                    print(" ||        0  ")
                if viedeb<=3:
                    print(" ||       /|\ ")
                if viedeb<=4:
                    print(" ||       /|  ")
                if viedeb<=5:
                    print(" ||           ")
                if viedeb<=6:
                    print(" ||           ")
                if viedeb<=7:
                    print(" ||           ")
                if viedeb<=8:
                    print("/||           ")
                if viedeb<=9:
                    print("==============\n")

            affichage = ""
            for x in solution:
                if x in lettres_trouvees:
                    affichage += x + " "
                else:
                    affichage += "_ "

            if "_" not in affichage:
                print(">>> Gagné! <<<")
                break
elif niveau == inter:
        
        while vieint > 0:
            print("Nombre de vie(s) :",vieint)
            print("\nMot à deviner : ", affichage)
            proposition = input("proposez une lettre : ")[0:1].lower()
            liste = liste + [proposition]
            print("lettre déja choisis : ",liste)

            if proposition in solution:
                lettres_trouvees = lettres_trouvees + proposition
                print("-> Bien vu!")
            else:
                vieint = vieint - 1
                print("-> Mauvaise réponse!\n")
                if vieint==0:
                    print(" ==========Y= ")
                    break
                if vieint<=1:
                    print(" ||/       |  ")
                if vieint<=2:
                    print(" ||        0  ")
                if vieint<=3:
                    print(" ||       /|\ ")
                if vieint<=4:
                    print(" ||       /|  ")
                if vieint<=5:
                    print("/||           ")
                if vieint<=6:
                    print("==============\n")

            affichage = ""
            for x in solution:
                if x in lettres_trouvees:
                    affichage += x + " "
                else:
                    affichage += "_ "

            if "_" not in affichage:
                print(">>> Gagné! <<<")
                break
elif niveau == exp:
        
        while viexp > 0:
            print("Nombre de vie(s) :",viexp)
            print("\nMot à deviner : ", affichage)
            proposition = input("proposez une lettre : ")[0:1].lower()
            liste = liste + [proposition]
            print(liste)

            if proposition in solution:
                lettres_trouvees = lettres_trouvees + proposition
                print("-> Bien vu!")
            else:
                viexp = viexp - 1
                print("-> Mauvaise réponse!\n")
                if viexp==0:
                    print(" ==========Y= ")
                    # break
                if viexp<=1:
                    print(" ||/       |  ")
                if viexp<=1:
                    print(" ||        0  ")
                if viexp<=2:
                    print(" ||       /|\ ")
                if viexp<=2:
                    print(" ||       /|  ")
                if viexp<=3:
                    print("/||           ")
                if viexp<=3:
                    print("==============\n")

            affichage = ""
            for x in solution:
                if x in lettres_trouvees:
                    affichage += x + " "
                else:
                    affichage += "_ "

            if "_" not in affichage:
                print(">>> Gagné! <<<")
                break

#while tentatives > 0:
#  print("\nMot à deviner : ", affichage)
#  proposition = input("proposez une lettre : ")[0:1].lower()
#
#  if proposition in solution:
#      lettres_trouvees = lettres_trouvees + proposition
#     print("-> Bien vu!")
#  else:
#    tentatives = tentatives - 1
#    print("-> Mauvaise réponse!\n")
#    if tentatives==0:
#        print(" ==========Y= ")
#    if tentatives<=1:
#       print(" ||/       |  ")
#   if tentatives<=2:
#         print(" ||        0  ")
#         if tentatives<=3:
#            print(" ||       /|\ ")
#         if tentatives<=4:
#          print(" ||       /|  ")
#    if tentatives<=5:
#        print("/||           ")
#    if tentatives<=6:
#        print("==============\n")

#  affichage = ""
#  for x in solution:
#      if x in lettres_trouvees:
#          affichage += x + " "
#      else:
#          affichage += "_ "

#  if "_" not in affichage:
#     print(">>> Gagné! <<<")
#     break

print("\n    * Fin de la partie *    ")