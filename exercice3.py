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
    extension = nom_fichier.split(".")[-1].lower()
    if extension == "txt":
        return True
    elif extension == "doc":
        return True
    elif extension == "pdf":
        return True
    else:
        return False

while True:
    nom_fichier = input("Entrez le nom du fichier (ou 'exit' pour quitter) : ")
    if nom_fichier.lower() == "exit":
        break
    if verifier_extension_fichier(nom_fichier):
        JoliePrint("L'extension est sécurisée.", 'v')
        break
    else:
        JoliePrint("L'extension n'est pas sécurisée.", 'r')
