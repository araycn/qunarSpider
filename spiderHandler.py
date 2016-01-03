# -*- coding: utf-8 -*-

from config import *
from mailSender import *
from easySpider import *
import time


class spiderHandle(object):
    def __init__(self):
        self.ticketInfo =""

    def getTicketInfo(self):
        qunar_spider = QunarSpider()
        return qunar_spider.get_ticket_info()

    def sendMessage(self,message):
        mail_sender= mailSender()
        mail_sender.sendMessage(message = message)

    def run(self):
        while True:
            self.ticketInfo = self.getTicketInfo()
            print "get ticket information %s" %self.ticketInfo
            if self.ticketInfo:
                succeed = self.sendMessage(self.ticketInfo)
                if succeed:
                    print "send message successfully !"
                else:
                    print "send message failed !"
            else :
                print "ticket not found, wait for the next query"
            time.sleep(CHECK_PERIOD)

if __name__ == "__main__":
    spider_handler = spiderHandle()
    spider_handler.run()



