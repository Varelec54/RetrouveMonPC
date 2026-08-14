#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests, sys, os, base64, smtplib, cv2, pyscreenshot
from datetime import datetime
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# --- CONFIGURATION (À REMPLACER VIA GÉNÉRATEUR) ---
CLE_SEC = "VOTRE_CLE_SECRETE"
U_CRYP  = "VOTRE_EMAIL_ENVOI_CRYPTE" 		# Compte Gmail expéditeur
P_CRYP  = "VOTRE_MOT_DE_PASSE_CRYPTE"		# Mot de passe d'application
D_CRYP  = "VOTRE_EMAIL_RECEP_CRYPTE" 		# Votre adresse de réception
IP_FIXE = "82.xx.xx.xx"              		# Votre IP personnelle
SMTP_SERVEUR = "smtp.gmail.com" 				# Par défaut
SMTP_PORT = 465                 				# 465 (SSL) ou 587 (TLS)

# ==========================================================
# 2. FONCTIONS DE DÉCODAGE
# ==========================================================
def decrypter(b64_text, key):
    raw = base64.b64decode(b64_text).decode()
    return "".join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(raw))

EMAIL_USER = decrypter(U_CRYP, CLE_SEC)
EMAIL_PASS = decrypter(P_CRYP, CLE_SEC)
EMAIL_DEST = decrypter(D_CRYP, CLE_SEC)

# ==========================================================
# 3. VÉRIFICATION DU RÉSEAU ET LOCALISATION
# ==========================================================
try:
    # Récupération de l'IP publique
    my_ip = requests.get('https://api.ipify.org', timeout=15).text
    
    # Si c'est votre IP habituelle, on arrête tout
    if my_ip == IP_FIXE:
        sys.exit()
    
    # Récupération des données de géolocalisation
    response = requests.get(f'http://ip-api.com/json/{my_ip}', timeout=15)
    info = response.json()
except:
    sys.exit() # Arrêt si pas d'internet ou erreur API

# ==========================================================
# 4. CAPTURES (ÉCRAN + WEBCAM)
# ==========================================================
sc_path, web_path = "sc.png", "web.png"

# Capture d'écran
try:
    pyscreenshot.grab().save(sc_path)
except:
    pass

# Photo Webcam (allumage très bref de la LED)
cap = cv2.VideoCapture(0)
if cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(web_path, frame)
    cap.release()

# ==========================================================
# 5. CONSTRUCTION DU RAPPORT DÉTAILLÉ
# ==========================================================
date_actuelle = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

rapport_details = f"""
==================================================
ALERTE DE SÉCURITÉ : CONNEXION PC DÉTECTÉE
==================================================
Date et Heure   : {date_actuelle}

INFOS RÉSEAU :
--------------
Adresse IP      : {my_ip}
Fournisseur Accès: {info.get('org', 'Non détecté')}
AS (Réseau)     : {info.get('as', 'Non détecté')}

GÉOLOCALISATION :
-----------------
Pays            : {info.get('country', 'Inconnu')}
Ville / CP      : {info.get('city', 'Inconnu')} ({info.get('zip', 'Inconnu')})
Région          : {info.get('regionName', 'Inconnue')}

COORDONNÉES GPS :
-----------------
Latitude        : {info.get('lat', 'Inconnue')}
Longitude       : {info.get('lon', 'Inconnue')}

LIEN GOOGLE MAPS :
https://www.google.com/maps?q={info.get('lat')},{info.get('lon')}
==================================================
Note : Les captures sont en pièces jointes.
"""

# ==========================================================
# 6. ENVOI DU MAIL (SSL PORT 465)
# ==========================================================
msg = MIMEMultipart()
msg["Subject"] = f"⚠️ ALERTE : PC localisé sur le réseau ({my_ip})"
msg["From"] = EMAIL_USER
msg["To"] = EMAIL_DEST

msg.attach(MIMEText(rapport_details, 'plain'))

# Attacher les images et les supprimer immédiatement du disque
for f_path in [sc_path, web_path]:
    if os.path.exists(f_path):
        with open(f_path, 'rb') as f:
            img = MIMEImage(f.read())
            img.add_header('Content-Disposition', 'attachment', filename=f_path)
            msg.attach(img)
        try:
            os.remove(f_path)
        except:
            pass

# Connexion au serveur Gmail et envoi
try:
    # Gestion automatique SSL (465) ou TLS (587)
    if SMTP_PORT == 465:
        with smtplib.SMTP_SSL(SMTP_SERVEUR, SMTP_PORT) as server:
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)
    else:
        with smtplib.SMTP(SMTP_SERVEUR, SMTP_PORT) as server:
            server.starttls() # Sécurisation de la connexion
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)
except Exception as e:
    pass