import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Gmail:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.port = 587
        self.expediteur = "dev.creusot.aym"
        self.password = "wssd dqtl hvyt onsy"

    def send_email(self, sujet, corps, destinataire):
        # Créer le message
        message = MIMEMultipart()
        message["From"] = self.expediteur + "@gmail.com"
        message["To"] = destinataire
        message["Subject"] = sujet
        # Ajouter le corps du message
        message.attach(MIMEText(corps, "plain"))
        with smtplib.SMTP(self.smtp_server, self.port) as serveur:
            serveur.starttls()

            # Se connecter au compte Gmail
            serveur.login(self.expediteur, self.password)

            # Envoyer l'e-mail
            serveur.sendmail(self.expediteur, destinataire, message.as_string())

            serveur.quit()
        print("L'e-mail a été envoyé avec succès.")
