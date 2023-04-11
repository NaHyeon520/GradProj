import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

import os

def send_mail(email, title, info, send_pic=False):#info: string converted from image
    print("send_mail called")
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('bik48154815@gmail.com', 'cknscchqmsgvalch')

    msg = MIMEMultipart()
    msg['Subject'] = '[2022 후기 졸업과제] 4조 프로젝트 테스트 이메일입니다.'#title
    content = MIMEText(info)
    msg.attach(content)
    '''
    filepath = "c:/Users/user/Desktop/GradProj-main/GradProj-main/0307.png"
    with open(filepath, 'rb') as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())  
        encoders.encode_base64(part) 
        part.add_header('Content-Disposition', 'attachment', filename=filepath)
        msg.attach(part)
    '''
    #addr = '4725hmc@gmail.com'
    # addr = "gbh4815@naver.com"#receiver
    #addr="hgcho@pusan.ac.kr"
    addr='rlaskgus520@gmail.com'
    msg["To"] = addr
    smtp.sendmail("bik48154815@gmail.com", addr, msg.as_string())
    print("send success")
    smtp.quit()
