from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
from bs4 import BeautifulSoup
import logging
import Utility
import time
from datetime import datetime

class ReverseProxy(BaseHTTPRequestHandler):
    def __init__(self):
        print("[Reverse Proxy-Server Inizialized...........]")
        print("[All Components are  Activated And Working Perfectly...........]")
        self.Load_Balancer=Utility.Inizialize_LoadBalancer()
        self.Load_Balancer=Utility.ConnectServerToReverseProxy(self.Load_Balancer)
        self.Cache=Utility.Initialize_Cache()
    
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin","*")
        self.send_header("Access-Control-Allow-Methods","*")
        self.send_header("Access-Control-Allow-Headers","*")
        self.end_headers()
    
    def do_GET(self):
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
    
    def do_POST(self):
        if self.path.endswith("Login"):
            self.Standard_Headers()
            Response=requests.post("https://google.com"+self.path)
            HTML_Response=BeautifulSoup(Response.text,'lxml')
            Response=Utility.Primary_Parser(HTML_Response)
            response=Response.prettify()
            self.wfile.write(bytes(response,"utf-8"))
        else:
            self.Standard_Headers(Type="image/jpeg")
            ImageBytes=requests.post(self.path[1:])
            self.wfile.write(ImageBytes.content)
    
    def do_PUT(self):
        self.Standard_Headers()
        Response=requests.put("https://google.com"+self.path)
        HTML_Response=BeautifulSoup(Response.text,'lxml')
        Response=Utility.Primary_Parser(HTML_Response)
        response=Response.prettify()
        self.wfile.write(bytes(response,"utf-8"))
    
    def do_DELETE(self):
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