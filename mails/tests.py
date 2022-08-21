import smtplib
from email.mime.text import MIMEText

from djangomails import settings


def send_email():
    try:
        # Creamos la conexion con servidor de correo
        mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        print(mailServer.ehlo())
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        
        email_to = 'gonzaloc1980@gmail.com'

        # Construimos el mensaje simple
        mensaje = MIMEText("""Mensaje de prueba de envio de correo simple con funcion MIMEText""")
        mensaje['From'] = settings.EMAIL_HOST_USER
        mensaje['To'] = email_to
        mensaje['Subject'] = "Tienes un correo"

        # Enviamos el correo
        mailServer.sendmail(settings.EMAIL_HOST_USER,
                            email_to,
                            mensaje.as_string())

        print('Correo enviado correctamente')

    except Exception as e:    # capturamos error
        print(e)


send_email()

