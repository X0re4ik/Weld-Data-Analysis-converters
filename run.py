from dotenv import load_dotenv

from notification_system.models import session
from notification_system.models import worker_sensor


from datetime import datetime

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

body = "This is an email with attachment sent from Python"


message = MIMEMultipart()
message["From"] = "Xore4ik@yandex.ru"
message["To"] = "Xore4ik@gmail.com"
message["Subject"] = "Это я"

# Add body to email
message.attach(MIMEText(body, "plain"))

if __name__ == '__main__':


    smtpObj = smtplib.SMTP_SSL('smtp.yandex.com')
    smtpObj.login('Xore4ik@yandex.ru','...')
    smtpObj.sendmail('Xore4ik@yandex.ru', 'Xoore4ik@gmail.com', message.as_string())

    smtpObj.quit()
    