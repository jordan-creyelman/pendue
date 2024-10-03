import random

def motAleatoire():
    mot = ["Montagne", "Étoile", "Voyage", "Chocolat", "Océan", 
           "Aventure", "Musique", "Nuage", "Sourire", "Lumière"]
    return mot[random.randint(0, len(mot) - 1)].lower()

mot = motAleatoire().lower()
array_lettre = []
mot_cacher = '* ' * len(mot)
tentative = 9

def info(mot, mot_cacher):
    print("La longueur du mot est " + str(len(mot)))
    print("Il reste " + str(mot_cacher.count("*")) + " lettres à trouver.")

def searchArrayList(lettre, array_lettre):
    if lettre in array_lettre:
        print("Lettre déjà tapée, choisis une autre lettre")
        return True  # La lettre a déjà été tapée
    else:
        array_lettre.append(lettre)  # Ajouter la lettre à la liste
        return False  # La lettre est nouvelle

def demander_lettre(array_lettre, mot_cacher, tentative):
    while True:
        if mot_cacher.count("*") > 0:
            if tentative > 0:
                lettre = input("Rentrer une lettre: ").lower()

                # Si la lettre est nouvelle, on la traite
                if not searchArrayList(lettre, array_lettre):
                    mot_cacher = play(mot, mot_cacher, lettre)
                    if lettre not in mot:
                        tentative -= 1  # Réduire les tentatives seulement si la lettre est incorrecte
                    print("Mot caché: " + mot_cacher)
                    print(f"Il te reste {tentative} tentatives.")
                    
                    # Appel de la méthode info ici
                    info(mot, mot_cacher)

                else:
                    print("Tu as déjà deviné cette lettre.")
            else:
                print("Perdu!")
                break
        else:
            print("Félicitations, tu as trouvé le mot!")
            break

def play(mot, mot_cacher, lettre):
    mot_split = list(mot)  # Liste des lettres du mot
    mot_cacher_split = mot_cacher.split(' ')  # Liste du mot caché (sans les espaces entre les lettres)
    
    trouver = False

    # Mise à jour du mot caché
    for index, x in enumerate(mot_split):
        if x == lettre:
            mot_cacher_split[index] = lettre  # Remplacer l'étoile par la lettre trouvée
            trouver = True

    if trouver:
        return ' '.join(mot_cacher_split)  # Reconstruire la chaîne avec des espaces entre les lettres
    else:
        print("Lettre non trouvée.")
        return mot_cacher

def game(array_lettre, mot_cacher, tentative):
    info(mot, mot_cacher)
    demander_lettre(array_lettre, mot_cacher, tentative)

game(array_lettre, mot_cacher, tentative)
