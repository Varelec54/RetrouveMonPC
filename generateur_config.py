#!/usr/bin/python3
# -*- coding: utf-8 -*-

import base64

def crypter(text, key):
    return base64.b64encode("".join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text)).encode()).decode()

print("==================================================")
print("   GÉNÉRATEUR DE CONFIGURATION - RETROUVEMONPC")
print("==================================================\n")

# Saisie des informations
cle = input("1. Choisissez une clé secrète (ex: MaClef123) : ")
user = input("2. Votre e-mail d'envoi (expéditeur) : ")
pw   = input("3. Mot de passe d'application (ou mot de passe mail) : ")
dest = input("4. Votre e-mail de réception (destinataire) : ")
ip   = input("5. Votre adresse IP actuelle (IP_FIXE) : ")
srv  = input("6. Serveur SMTP (ex: smtp.gmail.com) : ")
port = input("7. Port (465 pour SSL, 587 pour TLS) : ")

# Cryptage
u_cryp = crypter(user, cle)
p_cryp = crypter(pw, cle)
d_cryp = crypter(dest, cle)

print("\n" + "="*50)
print("   COPIEZ LE BLOC CI-DESSOUS DANS RETROUVE_PC.PY")
print("="*50 + "\n")

print(f'CLE_SEC = "{cle}"')
print(f'U_CRYP  = "{u_cryp}"')
print(f'P_CRYP  = "{p_cryp}"')
print(f'D_CRYP  = "{d_cryp}"')
print(f'IP_FIXE = "{ip}"')
print(f'SMTP_SERVEUR = "{srv}"')
print(f'SMTP_PORT = {port}')

print("\n" + "="*50)
print("Gardez votre clé secrète précieusement.")
input("\nAppuyez sur Entrée pour quitter...")