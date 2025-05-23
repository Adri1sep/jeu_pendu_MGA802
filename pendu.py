#JEU DU PENDU

#importation des bibliotheques
import random as rd

#FONCTIONS

#choix de mot dans le fichier
def choisir_mot():
    #lire le fichier (preciser l’encoding pour les accents)
    f=open("mots_pendu.txt","r",encoding='utf-8')
    #recuperation des mots sous forme de liste
    mots = f.read().split("\n")
    #choix aléatoire
    mot=mots[rd.randint(0,len(mots)-1)]
    f.close()
    return mot

#affichage
def afficher_jeu(a,b):
    #afficher le mot et les vies
    print(a+"               "+str(b)+" vies restantes\n \n   +---+   ")
    #dessiner le pendu
    if b==1:
        #on rejoute ici r devant certaines str pour éviter l’erreur invalid escape sequence '\ '
        print("   0   |\n  /|"+r"\ "+" |\n  /    |")
    elif b==2:
        print("   0   |\n  /|"+r"\ "+" |\n       |")
    elif b==3:
        print("   0   |\n  /|   |\n       |")
    elif b==4:
        print("   0   |\n   |   |\n       |")
    elif b==5:
        print("   0   |\n       |\n       |")
    elif b==6:
        print("       |\n       |\n       |")
    print("      -|-")

#trouver position lettre
def trouver_lettre(mot,lettre):
    indices=[]
    for i in range(len(mot)):
        if mot[i]==lettre:
            indices.append(i)
    return indices

#proposition de lettre (regler probleme accents)
def proposer_lettre(c,d):
    lettre=input("\nEntrez une lettre: ")
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #test de validité de l’input
    if lettre in alphabet:
        #gestion des cas
        cas=[]
        #test si la lettre est directement dans le mot
        if lettre in c:
            #recuperation des indices de position
            liste_indices=trouver_lettre(c,lettre)
            #modification de a_completer
            for i in liste_indices:
                #on passe par une liste pour modifier le mot a completer
                d_liste=list(d)
                d_liste[i]=lettre
                d="".join(d_liste)
            #premier cas
            cas.append(1)
        #test si des accents de la lettre sont présents
        if lettre in ["a","e","i","o","u"]:
            liste_indices=[]
            if lettre=="e":
                for i in ["è", "é", "ê", "ë"]:
                    if trouver_lettre(c,i) != []:
                        for y in trouver_lettre(c,i):
                            liste_indices.append(y)
                        lettre=i
            elif lettre=="a":
                for i in ["à", "ä", "â"]:
                    if trouver_lettre(c,i) != []:
                        for y in trouver_lettre(c, i):
                            liste_indices.append(y)
                        lettre=i
            elif lettre=="i":
                for i in ["î", "ï"]:
                    if trouver_lettre(c,i) != []:
                        for y in trouver_lettre(c, i):
                            liste_indices.append(y)
                        lettre=i
            elif lettre=="o":
                for i in ["ö", "ô"]:
                    if trouver_lettre(c,i) != []:
                        for y in trouver_lettre(c, i):
                            liste_indices.append(y)
                        lettre=i
            elif lettre=="u":
                for i in ["ü", "ù", "û"]:
                    if trouver_lettre(c,i) != []:
                        for y in trouver_lettre(c, i):
                            liste_indices.append(y)
                        lettre=i
            #de maniere analogue a la boucle précédente
            for i in liste_indices:
                d_liste=list(d)
                d_liste[i]=lettre
                d="".join(d_liste)
            #on enonce les resultats du test
            if liste_indices!=[]:
                #second cas
                cas.append(2)
            else:
                #3eme cas
                cas.append(3)
        if (not(lettre in c) and not(lettre in ["a","e","i","o","u"])) or (1 not in cas and 3 in cas):
            print("\nCette lettre n'est pas dans le mot.\n")
            # on renvoie la reussite,le mot a completer si il a été changé et enfin la lettre proposée pour garder en mémoir
            return [False, 0, lettre]
        #return si un des deux cas
        if 1 or 2 in cas:
            print("\nCette lettre est bien contenue dans le mot.\n")
            return [True, d, lettre]
    else:
        print("Cette lettre n´est pas valide.\n")
        return [False,0,lettre]

#jeu
def executer_jeu():
    while True:
        #initialisation, choix du mot
        memoire = []
        print("\nBienvenue sur le jeu du pendu, un mot a été choisi parmi ceux du fichier texte fourni, le voici incomplet:\n")
        mot_a_deviner=choisir_mot()
        mot_a_deviner="éteindre"
        # definition du mot a trou
        a_completer = '_' * len(mot_a_deviner)
        vies=6
        while vies>0 :
            #affichage
            afficher_jeu(a_completer,vies)
            #proposition de lettre
            prop=proposer_lettre(mot_a_deviner,a_completer)
            if prop[0]==True:
                # on met a jour le mot a completer
                a_completer = prop[1]
            else:
                vies -= 1
            #stocker dans la mémoire des lettres proposées
            memoire.append(prop[2])
            #test de victoire
            if "_" not in a_completer:
                print("Félicitations! Vous avez gagné avec "+str(vies)+" vies restantes!")
                break
            #aide
            if vies==1:
                print("Voici pour vous aider les lettres que vous avez déja proposé:")
                print(*memoire)
            #test de défaite
            if vies==0:
                print("\nVous avez perdu! Le mot était "+mot_a_deviner+".")
                #afficher le pendu
                print("   +---+\n   0   |\n"+r"  /|\  |"+"\n  / "+r"\ "+" |\n      -|-")
                break
        #demande pour quitter ou rejouer
        demande=input("\nTapez 1 pour rejouer ou une autre touche pour quitter:")
        if demande=="1":
            continue
        else:
            break


#EXECUTION
executer_jeu()