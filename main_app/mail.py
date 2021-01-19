import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64



# Before using your email,  please ensure that you have set you gmail account to enable "less secure apps"
# Recheck this step that you have enabled the less secure app

def send_email(name, dest, link):
    server = smtplib.SMTP('smtp.gmail.com', 587)   #Gmail SMTP port (TLS)
    server.starttls()

    # Enter your Email and Password
    server.login("achyut662cs@gmail.com", "662cs@12345")
    email_html = open('main_app/templates/main_app/email.html')
    email_body = email_html.read().format(name=name, link=link)
    msg = MIMEMultipart()
    msg['Subject'] = 'EMERGENCY'
    msg.attach(MIMEText(email_body, 'html'))
    
    # Again enter your Email ID
    msg['From'] = formataddr(("TEAM RESCUE", "achyut662cs@gmail.com"))

    # One last time add your email
    server.sendmail("achyut662cs@gmail.com", dest, msg.as_string())
    server.quit()