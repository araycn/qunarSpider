import smtplib
from config import *
from email.mime.text import MIMEText


class mailSender(object):
    def __init__(self, smtp_server = MAIL_SERVER,
                 usrname = MAIL_USRNAME,
                 password = MAIL_PASSWORD):
        try:
            print "setting connection to %s" %MAIL_SERVER
            self.smtp_server = smtplib.SMTP(MAIL_SERVER)
            self.smtp_server.login(usrname,password)

        except Exception, e:
            print e
            print "connection closing..."
            self.smtp_server.close()

    def sendMessage(self,usrname = MAIL_USRNAME,
                    target = MAIL_TARGET,
                    message = ""):
        try:
            print "sending message:%s" %message
            self.smtp_server.sendmail(usrname+"@126.com", target, message)
            return True
        except Exception, e:
            print "sending problem occured ...closing it"
            self.smtp_server.close()
            print e
            return False

if __name__ == "__main__":
    mailSender = mailSender()
    print mailSender.sendMessage(message = "hi dubin, take a view")
