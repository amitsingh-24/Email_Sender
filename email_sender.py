import smtplib

to = input("Enter the email of recipient:\n")

content = input("Enter the content of mail:\n")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('senderemail@gmail.com','1234')
    server.sendEmail('senderemail@gmail.com',to,content)
    server.close()

sendEmail(to,content)
