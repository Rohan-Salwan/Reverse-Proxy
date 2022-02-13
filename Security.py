import logging
import re
from datetime import datetime

class Security:
    def __init__(self):
        self.BlackList={"char","nchar","varchar","nvarchar","alter","begin","cast","create",
        "cursor","declare","delete","drop","end","exec","execute","fetch","insert","kill","open",
        "select","sys","sysobjects","syscolumns","table","update","sleep","uid",
        "waitfor","delay","system","union","order by","group by","<script>","--"}
        self.SpecialChar={" ","'","}","{",")","(","|","*",";","@","<",">","$","!"}
        self.logger=logging
        self.logger.basicConfig(filename="Logs.txt",level=logging.DEBUG,format = '%(asctime)s %(levelname)s %(name)s %(message)s')
        self.RequestTimeRecord={}
        self.BlockList=set()
        self.Record=[]
    
    def Input_Sanitizer(self,url,Ip):
        for char in self.BlackList:
            if char in url:
                self.logger.debug(url)
                StartingIndex=url.index(char)
                finishingIndex=StartingIndex+len(char)
                url=url[:StartingIndex-1]+url[finishingIndex:]
                self.logger.debug(Ip+"\n"+"Intrusion Detected\n"+char+"   "+"SQL Injection Attack Detected\n"+"Malicious Keyword Found")
        for char in url:
            if char in self.SpecialChar:
                self.logger.debug(url)
                url=url.replace(char,"")
                self.logger.debug("Intrusion Detected\n"+char+"     "+"Malicious Keyword Found")    
        return url

    def PreventBrute_Force(self,IP):
        Local_Time=datetime.now()
        Local_Time=Local_Time.strftime("%M")
        Local_Time=int(Local_Time)
        if len(self.Record)>0:
            ExIp=self.Record[0]
            requestlist=self.RequestTimeRecord[ExIp]
            if Local_Time>=requestlist[0]+4 and requestlist[1]<30:
                del self.RequestTimeRecord[IP]
                self.Record.pop(0)
        if IP in self.BlockList:
            return "Blocked_IP_Address"
        elif IP in self.RequestTimeRecord:
            IPRequestlist=self.RequestTimeRecord[IP]
            if Local_Time>=IPRequestlist[0]+4 and IPRequestlist[1]>30:
                self.BlockList.add(IP)
                self.logger.debug("BRUTE FORCE ATTACK DETECTED BY"+IP)
                self.logger.debug("IP Address"+IP+"Got Blocked by System")
                del self.RequestTimeRecord[IP]
            else:
                value=self.RequestTimeRecord[IP][1]
                self.RequestTimeRecord[IP][1]=value+1
                self.Record.append(IP)
        else:
            Local_Time=int(Local_Time)
            self.RequestTimeRecord[IP]=[Local_Time,0]

    


