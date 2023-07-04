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
        print(rouge, emojis['r'], " ", message, reset)
    elif code == 'v':
        print(vert, emojis['v'], " ", message, reset)

def ip_valide(adresse_ip):
    octets = adresse_ip.split(".")
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit():
            return False
        if int(octet) < 0:
            return False
        if int(octet) > 255:
            return False
    return True

def convertir_en_binaire(adresse_ip):
    octets = adresse_ip.split(".")
    octets_binaires = []
    for octet in octets:
        if not octet.isdigit():
            octet_binaire = 'INVALID'
        elif int(octet) < 0:
            octet_binaire = 'INVALID'
        elif int(octet) > 255:
            octet_binaire = 'INVALID'
        else:
            octet_binaire = format(int(octet), '08b')
            octets_binaires.append(str(octet_binaire))
        adresse_ip_binaire = ".".join(octets_binaires)
    return adresse_ip_binaire

while True:
    adresse_ip = input("💾 👉 Entrez une adresse IP Exemple:'192.168.0.1'\n(ou 'exit', pour quitter) : ")
    if adresse_ip.lower() == "exit":
        break

    if not ip_valide(adresse_ip):
        JoliePrint("Adresse IP invalide. Veuillez entrer une adresse IP valide.", 'r')
        continue

    adresse_ip_binaire = convertir_en_binaire(adresse_ip)
    JoliePrint("Adresse IP en binaire : " + adresse_ip_binaire, 'v')
    break