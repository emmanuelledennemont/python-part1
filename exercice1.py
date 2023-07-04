#!/usr/bin/python3

def JoliePrint(resultat):
    rouge = "\033[31m"
    vert = "\033[32m"
    reset = "\033[0m"
    
    emojis = {
        True: '😆',
        False: '😖',
    }
    
    if resultat:
        print(vert, emojis[resultat], "Mot de passe valide.", reset)
    else:
        print(rouge, emojis[resultat], "Mot de passe invalide.", reset)

def verifier_mot_de_passe(mot_de_passe):
    if len(mot_de_passe) < 8:
        return False
    elif mot_de_passe.islower():
        return False
    elif mot_de_passe.isupper():
        return False
    elif mot_de_passe.isalpha():
        return False
    elif mot_de_passe.isdigit():
        return False
    else:
        return True

mot_de_passe_valide = False

while not mot_de_passe_valide:
    mot_de_passe = input("\t1️⃣ Le mot de passe doit contenir au moins 8 caractères.\n\t1️⃣ Le mot de passe doit contenir au moins une lettre majuscule et une lettre minuscule.\n\t3️⃣ Le mot de passe doit contenir au moins un chiffre.\n🔑 Entrez votre mot de passe : ")

    resultat_verification = verifier_mot_de_passe(mot_de_passe)

    JoliePrint(resultat_verification)
    
    if resultat_verification:
        mot_de_passe_valide = True
    else:
        choix = input("Voulez-vous essayer un autre mot de passe ? (Oui/Non) : ")
        while choix.lower() not in ["oui", "non"]:
            choix = input("Veuillez répondre par 🟢'Oui' ou 🔴'Non' : ")
        if choix.lower() != "oui":
            break
