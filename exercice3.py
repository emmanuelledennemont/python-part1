#!/usr/bin/python3

def JoliePrint(message, code='r'):
    rouge = "\033[31m"
    vert = "\033[32m"
    reset = "\033[0m"
    
    emojis = {
        'r': '❌',
        'v': '✅',
    }
    
    if code == 'r':
        print(rouge, emojis['r'], message, reset)
    elif code == 'v':
        print(vert, emojis['v'], message, reset)

def verifier_extension_fichier(nom_fichier):
    extension = nom_fichier.split(".")[-1]

    if extension.islower() and extension in ["pdf", "txt", "doc"]:
        return True
    else:
        return False
    
nouveau_fichier = True

while nouveau_fichier:
    nom_fichier = input("💾 👉 Entrez le nom du fichier : ")

    resultat_verification = verifier_extension_fichier(nom_fichier)

    if resultat_verification:
        JoliePrint(f"Le nom du fichier '{nom_fichier}' est valide.", 'v')
        JoliePrint(True, 'v')
    else:
        JoliePrint(f"Le nom du fichier '{nom_fichier}' est invalide.", 'r')
        JoliePrint(False, 'r')
    
    choix = input("Voulez-vous essayer un autre nom de fichier ? (Oui/Non) : ")
    
    while choix.lower() not in ["oui", "non"]:
        choix = input("Veuillez répondre par 🟢'Oui' ou 🔴'Non' : ")
    
    if choix.lower() != "oui":
        nouveau_fichier = False

    