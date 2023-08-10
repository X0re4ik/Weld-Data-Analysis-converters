from dotenv import load_dotenv

from notification_system.models import session
from notification_system.models import (
    worker_sensor,
    NotificationDate, 
    Worker,
    Measurement,
    Sensor, DailyReport,
    WeldingWireDiameter,
    WeldMetal
)


from datetime import datetime, timedelta, date

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


import random

from openpyxl import Workbook, load_workbook


# # grab the active worksheet
# ws = wb.active


# Data can be assigned directly to cells
from sqlalchemy import and_, func






from notification_system.сonverters.to_excel import MeasurementsToExcelConverter


m = MeasurementsToExcelConverter("RW-tnlvnegclxzc", date=date(2023, 7, 28))
m.load_from_DB(session=session)
m.write_measurements()
m.save()
