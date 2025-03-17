import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pages.variables.teardownProcess_variables import *


def send_report(filename):
    sender = sender_mail
    receiver = receiver_mail
    password = app_key

    msg = MIMEMultipart()
    msg['Subject'] = 'AMAZON AUTOMATION TEST REPORT'
    msg['From'] = sender
    msg['To'] = receiver
    body_part = MIMEText('HTML Report for the test cases is attached below!')
    msg.attach(body_part)

    filename = filename

    with open(filename, 'r') as f:
        part = MIMEBase("application", "octet-stram")
        part.set_payload(f.read())

    part.add_header(
        "Content-Disposition",
        f'attachment; filename={filename}',
    )
    msg.attach(part)
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(sender, password)

        smtp.sendmail(sender, receiver, msg.as_string())

        smtp.quit()