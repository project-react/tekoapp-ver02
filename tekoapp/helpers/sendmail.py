import config
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def config_mail_verify(subject, content_msg, des_mail):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = config.FLASK_APP_MAIL_ADRESS
    msg['To'] = des_mail
    msg.attach(MIMEText(content_msg, 'html'))
    print(des_mail)
    return msg

def send_mail(subject, content_msg, des_mail, type=""):
    if(type != 'verify'): 
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(config.FLASK_APP_MAIL_ADRESS, config.FLASK_APP_MAIL_PASSWORD)
            message = 'Subject: {}\n\n{}'.format(subject, content_msg)
            server.sendmail(config.FLASK_APP_MAIL_ADRESS, des_mail, message)
            server.quit()
            return True
        except:
            return False
    else:
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(config.FLASK_APP_MAIL_ADRESS, config.FLASK_APP_MAIL_PASSWORD)
            message = config_mail_verify(subject, content_msg, des_mail)
            server.sendmail(config.FLASK_APP_MAIL_ADRESS, des_mail, message.as_string())
            server.quit()
            return True
        except:
            return False