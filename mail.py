import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
f = open('send1.txt','r')

def SendMail(ImgFileName):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'AUTOMATED PHOTOBOOTH @JUIT'
    From = 'ieee.photobooth@gmail.com'
    text = MIMEText("Thank you for being a part of it.Hope you enjoyed :)\n\n\n\n\n\n\n\n\n-IEEE ThinkLab")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)
    Server='smtp.gmail.com'
    Port='587'
    
    s = smtplib.SMTP(Server, Port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    UserName='ieee.photobooth'
    UserPassword='clickphoto'
    s.login(UserName, UserPassword)
    """while True:
        To = f.readline()
        print(To)
        if not To:
            break"""
    To = f.readline()
    print(To)
    print("Sending")
    s.sendmail(From, To, msg.as_string()) 
    s.quit()
    print("Sent")
SendMail('capt0000.jpg')


