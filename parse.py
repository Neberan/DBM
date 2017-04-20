import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Ces variables sservent à l'envoi de mail
mail_envoi = input("Entrez adresse mail")
mail_desti = input("Entrez le destinataire")
password = input("Mot de passe")


f = open('ssh.log', 'r')
for ligne in f:
    line = ligne.strip(':')
    date = ligne[:16]
    server = ligne[16:35]
    statut = ligne[36:]
    w = open('extrat', 'a')
    w.write(date + server + statut + "\n")

def mail():

    msg = MIMEMultipart()
    msg['From'] = mail_envoi
    msg['To'] = mail_desti
    msg['Subject'] = 'Ceci est un test'
    message = 'Bonjour !'
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(mail_envoi, password)
    mailserver.sendmail(mail_envoi, mail_envoi, msg.as_string())
    mailserver.quit()
mail()
w.close()
f.close()

