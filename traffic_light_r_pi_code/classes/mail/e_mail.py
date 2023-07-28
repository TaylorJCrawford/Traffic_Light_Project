from classes.mail.e_mail_template import build_html, htmlClass

import smtplib, os, datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import urllib.request, json

from classes.common import CommonFunctions

class EmailClass:

    def __init__(self, path):
        # os.path.normpath()
        tempClass = CommonFunctions()
        SystemPath = tempClass.get_path()#"/home/pi/test-python/"
        with open(SystemPath + "assets/config.json", "r") as jsonFile:
            data = json.load(jsonFile)

        self.SenderEmailAddress = data['SenderEmailAddress']
        self.SenderEmailPassword = data['SenderEmailPassword']
        self.ReceiverEmailAddress = data['ReceiverEmailAddress']

    def send_email(self, message_code, header_image='/assets/mail_icon.png'):

        dir_root = os.path.dirname(os.path.abspath(__file__))
        msg = MIMEMultipart('related')

        html_class = htmlClass()

        body_content = '<h1>Error - Could Not Handle Request,<br>Please Contact Support</h1>'
        heading = 'Error'
        subject = 'Error'

        if message_code == 0:
            heading = ''
            subject = 'Computer Help, Please'
            message = 'Need Your Help, With My Computer!'
            body_content = html_class.build_html_code_message(message)
        elif message_code ==  1:
            heading = ''
            subject = 'Emergency - SOS'
            message = 'Really Need Your Help - Defcon 1.'
            body_content = html_class.build_html_code_message(message)
        elif message_code == 2:
            heading = ''
            subject = 'Feed Horses '
            message = 'Can You Feed The Horses?'
            body_content = html_class.build_html_code_message(message)

        html = build_html(heading, body_content)

        msg = MIMEMultipart('related')
        msg['Subject'] = subject
        msg['From'] = self.SenderEmailAddress
        msg['To'] = self.ReceiverEmailAddress

        msgText = MIMEText(html, 'html')
        msg.attach(msgText)

        # This example assumes the image is in the current directory
        dir_root = os.path.dirname(os.path.abspath(__file__))

        fp = open(dir_root + header_image, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        # Define the image's ID as referenced above
        msgImage.add_header('Content-ID', '<image1>')
        msg.attach(msgImage)

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo() # ID to server
            smtp.starttls() # Start encryption
            smtp.ehlo() # ID to server again due to starting encryption

            smtp.login(self.SenderEmailAddress, self.SenderEmailPassword)
            smtp.send_message(msg)