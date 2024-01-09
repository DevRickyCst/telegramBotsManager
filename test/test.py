import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def envoyer_email(destinataire, sujet, corps, expediteur, mot_de_passe):
    # Configurer le serveur SMTP de Gmail
    smtp_server = "smtp.gmail.com"
    port = 587  # Utilisez le port 465 pour SSL

    # Créer le message
    message = MIMEMultipart()
    message["From"] = expediteur + "@gmail.com"
    message["To"] = destinataire
    message["Subject"] = sujet

    # Ajouter le corps du message
    message.attach(MIMEText(corps, "plain"))

    # Établir une connexion sécurisée avec le serveur SMTP
    with smtplib.SMTP(smtp_server, port) as serveur:
        serveur.starttls()

        # Se connecter au compte Gmail
        serveur.login(expediteur, mot_de_passe)

        # Envoyer l'e-mail
        serveur.sendmail(expediteur, destinataire, message.as_string())

        serveur.quit()
    print("L'e-mail a été envoyé avec succès.")


# Remplacez ces valeurs par vos propres informations
destinataire = "creusot.aymeric7@gmail.com"
sujet = "Test d'envoi d'e-mail avec Python"
corps = "Ceci est un exemple d'e-mail envoyé depuis Python."
expediteur = "dev.creusot.aym"
mot_de_passe = "wssd dqtl hvyt onsy"
# wssd dqtl hvyt onsy

envoyer_email(destinataire, sujet, corps, expediteur, mot_de_passe)
