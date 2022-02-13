from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
from bs4 import BeautifulSoup
import logging
from Security import Security
import Utility
import time
from datetime import datetime
import cgi

class ReverseProxy(BaseHTTPRequestHandler):
    Load_Balancer=Utility.Inizialize_LoadBalancer()
    Cache=Utility.Initialize_Cache()
    logger=logging
    logger.basicConfig(filename="Logs.txt",level=logging.DEBUG,format = '%(asctime)s %(levelname)s %(name)s %(message)s')
    Security=Security()
    print("[Reverse Proxy-Server Inizialized...........]")
    print("[All Components are  Activated And Working Perfectly...........]")
    logger.debug("[Reverse Proxy-Server Inizialized...........]")
    logger.debug("[All Components are  Activated And Working Perfectly...........]")
    
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin","*")
        self.send_header("Access-Control-Allow-Methods","*")
        self.send_header("Access-Control-Allow-Headers","*")
        self.end_headers()
    
    def do_GET(self):
        Client_Addr=self.client_address[0]
        Validation=self.Security.PreventBrute_Force(Client_Addr)
        if Validation==None:
            ServerIP=self.Load_Balancer.Get_ServerIP(Client_Addr)
            self.path=self.Security.Input_Sanitizer(self.path,Client_Addr)
            if "images" in self.path and ".png" not in self.path:
                self.Standard_Headers(Type="image/jpeg")
                ImageBytes=requests.get(self.path[1:])
                self.wfile.write(ImageBytes.content)
            else:
                self.Standard_Headers()
                Response=requests.get("https://google.com"+self.path)
                HTML_Response=BeautifulSoup(Response.text,'lxml')
                Response=Utility.Primary_Parser(HTML_Response)
                response=Response.prettify()
                self.wfile.write(bytes(response,"utf-8"))
        else:
            self.Standard_Headers(type="text/html")
            response="<html>IP"+Client_Addr+"got blocked by system</html>"
            self.wfile.write(bytes(response,"utf-8"))
    
    def do_POST(self):
        Client_Addr=self.client_address[0]
        Validation=self.Security.PreventBrute_Force(Client_Addr)
        if Validation==None:
            ServerIP=self.Load_Balancer.Get_ServerIP(Client_Addr)
            self.path=self.Security.Input_Sanitizer(self.path,self.client_address)
            if self.path.endswith("/Login"):
                ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
                pdict['boudary']=bytes(pdict['boundary'],"utf-8")
                ContentLength=int(self.headers.get('Content-length'))
                pdict['CONTENT-LENGTH']=ContentLength
                if ctype=='multipart/form-data':
                    Fields=cgi.parse_multipart(self.rfile,pdict)
                    Email=Fields.get('Email')
                    Password=Fields.get('Password')
                    self.responses(200)
                    self.send_header('content-type','text/html')
                    self.end_headers() 
                    PayLoad={"Email":Email, "Password":Password}
                    Response=requests.post("https://google.com"+self.path,data=PayLoad)
                    HTML_Response=BeautifulSoup(Response.text,'lxml')
                    Response=Utility.Primary_Parser(HTML_Response)
                    response=Response.prettify()
                    self.wfile.write(bytes(response,"utf-8"))
        else:
            self.Standard_Headers(type="text/html")
            response="<html>IP"+Client_Addr+"got blocked by system</html>"
            self.wfile.write(bytes(response,"utf-8"))

    def do_PUT(self):
        self.path=self.Security.Input_Sanitizer(self.path,self.client_address[0])
        self.Standard_Headers()
        Response=requests.put("https://google.com"+self.path)
        HTML_Response=BeautifulSoup(Response.text,'lxml')
        Response=Utility.Primary_Parser(HTML_Response)
        response=Response.prettify()
        self.wfile.write(bytes(response,"utf-8"))
    
    def do_DELETE(self):
        self.path=self.Security.Input_Sanitizer(self.path,self.client_address[0])
        self.Standard_Headers()
        Response=requests.delete("https://google.com"+self.path)
        HTML_Response=BeautifulSoup(Response.text,'lxml')
        Response=Utility.Primary_Parser(HTML_Response)
        response=Response.prettify()
        self.wfile.write(bytes(response,"utf-8"))

    def Standard_Headers(self,Type="text/html"):
        self.send_response(200)
        self.send_header("content-type",Type)
        Local_Time=datetime.now()
        Local_Time=Local_Time.strftime("%H:%M:%S")
        date=time.strftime("%d %b %Y ")
        self.send_header("User-Entry-Time",Local_Time)
        self.send_header("User-Entry-Date",date)
        self.end_headers()
            

http=HTTPServer(('localhost',8080),ReverseProxy)
http.serve_forever()