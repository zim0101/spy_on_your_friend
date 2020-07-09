import os
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from settings import (SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL)


def prepare_mail(ImgFileName):
    """
    Prepare mail content
    :rtype: object
    """
    img_data = open(ImgFileName, 'rb').read()
    message = MIMEMultipart()
    message['Subject'] = 'SPY!'
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    message.attach(image)

    return message


def send_mail(ImgFileName):
    """
    Send the email
    :rtype: object
    """
    mail = prepare_mail(ImgFileName)
    mailer = smtplib.SMTP('smtp.gmail.com', 587)
    mailer.ehlo()
    mailer.starttls()
    mailer.ehlo()
    mailer.login(SENDER_EMAIL, SENDER_PASSWORD)
    mailer.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, mail.as_string())
    mailer.quit()
