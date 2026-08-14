
===========================================================
    SYSTÈME DE SURVEILLANCE ET LOCALISATION PC v1.0
          Site : http://retrouver.son.pc.free.fr/
===========================================================

Ce pack contient un ensemble de scripts Python permettant de 
localiser votre ordinateur et de recevoir une capture d'écran 
ainsi qu'une photo webcam en cas d'utilisation par un tiers.

--- CONTENU DU PACK ---

1. RetrouveMonPC.py        : Le script principal (coeur du système).
2. lanceur.py          : Le gestionnaire qui tourne en boucle.
3. generateur_config.py: Outil pour chiffrer vos identifiants.
4. test_mail.py        : Utilitaire pour vérifier la connexion.

--- INSTALLATION (ÉTAPE PAR ÉTAPE) ---

1. Installez Python 3 (disponible sur python.org).
2. Ouvrez un terminal (Linux) ou une invite de commande (Windows).
3. Installez les dépendances nécessaires avec la commande :
   pip install requests pyscreenshot opencv-python Pillow

--- CONFIGURATION ---

1. GÉNÉRATION DES ACCÈS :
   Lancez 'generateur_config.py'. Saisissez une clé secrète, 
   votre e-mail d'envoi (expéditeur), son mot de passe 
   d'application, et votre e-mail de réception. 
   Copiez scrupuleusement les codes générés.

2. PARAMÉTRAGE DU SCRIPT :
   Ouvrez 'RetrouveMonPC_pc.py' avec un éditeur de texte. 
   - Collez vos codes (CLE_SEC, U_CRYP, P_CRYP, D_CRYP).
   - Modifiez IP_FIXE avec votre adresse IP actuelle pour 
     éviter de vous auto-alerter quand vous êtes chez vous.

3. TEST :
   Lancez 'test_mail.py' pour vérifier que l'alerte arrive 
   bien dans votre boîte de réception.

--- UTILISATION ---

> Sous Windows :
Double-cliquez sur 'lanceur.py'. 
Astuce : Renommez-le en 'lanceur.pyw' pour qu'il s'exécute de 
manière totalement invisible (sans fenêtre noire). Ajoutez un
raccourci dans votre dossier "Démarrage" pour l'automatiser.

> Sous Linux :
Lancez la commande : python3 lanceur.py
Pour une surveillance automatique, ajoutez 'lanceur.py' à votre 
liste d'applications au démarrage (Session et démarrage).

--- SÉCURITÉ ET CONFIDENTIALITÉ ---

- Ce script est destiné à un usage personnel uniquement.
- Les photos prises sont supprimées du disque dur immédiatement 
  après l'envoi de l'e-mail pour ne laisser aucune trace.
- Le script n'envoie des données qu'à l'API de localisation 
  publique (ip-api.com) et à votre propre serveur mail.
  
--- ⚠️ AVERTISSEMENT SÉCURITÉ IMPORTANT ⚠️ ---

Le chiffrement XOR utilisé protège vos identifiants contre les 
robots et les analyses automatiques. Cependant, pour une 
sécurité maximale, nous vous RECOMMANDONS FORTEMENT de :
- Créer un compte mail DÉDIÉ uniquement à ce script.
- Ne jamais utiliser votre compte e-mail personnel principal 
  pour l'envoi des alertes.
- Ainsi, même si vos accès étaient déchiffrés par un expert, 
  vos données personnelles resteraient totalement à l'abri.

===========================================================
L'auteur décline toute responsabilité en cas d'usage illégal.
Pour toute aide supplémentaire : http://retrouver.son.pc.free.fr/
===========================================================
