import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
    msg['From'] = 'johann77166@gmail.com'
    msg['To'] = 'moulart.johann@outlook.com'
    msg['Subject'] = 'Ceci est un test'
    message = 'Bonjour !'
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('johann77166@gmail.com', 'Crousty1')
    mailserver.sendmail('johann77166@gmail.com', 'johann77166@gmail.com', msg.as_string())
    mailserver.quit()
mail()
w.close()
f.close()

