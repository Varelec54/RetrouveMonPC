import smtplib, base64

# Copiez vos variables ici pour tester
CLE_SEC = "VOTRE_CLE_SECRETE"
U_CRYP  = "VOTRE_EMAIL_ENVOI_CRYPTE" 		# Compte Gmail expéditeur
P_CRYP  = "VOTRE_MOT_DE_PASSE_CRYPTE"		# Mot de passe d'application
D_CRYP  = "VOTRE_EMAIL_RECEP_CRYPTE" 		# Votre adresse de réception

def decrypter(b, k):
    r = base64.b64decode(b).decode()
    return "".join(chr(ord(c) ^ ord(k[i % len(k)])) for i, c in enumerate(r))

try:
    u, p = decrypter(U_CRYP, CLE_SEC), decrypter(P_CRYP, CLE_SEC)
    s = smtplib.SMTP_SSL("smtp.gmail.com", 465)   # Remplacez 
    print("Succès ! Connexion établie.")
    s.quit()
except Exception as e:
    print(f"Erreur : {e}")
input("Fin du test...")