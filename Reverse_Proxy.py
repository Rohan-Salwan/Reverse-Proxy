import socket
import threading
import logging
from . import LoadBalancer


class ReverseProxy:
    def __init__(self):
        Server_Adderess=""
        Server_Port = int(input("Please provide port"))
        ReverseProxy_ServerSocket=self.Build_Socket()
        ReverseProxy_ServerSocket.bind((Server_Adderess,Server_Port))
        ReverseProxy_ServerSocket.listen(5)
        self.Inizialize_LoadBalancer()
        self.Main(ReverseProxy_ServerSocket)

    def Main(self,ProxyServer_Socket):
        while True:
            Client_Socket, Client_Address=ProxyServer_Socket.accept()
            Thread=threading.Thread(target=self.Mediator_BTW_ClientAndServers,args=(Client_Socket,Client_Address))
            Thread.start()    
    
    def Mediator_BTW_ClientAndServers(self,Client_Socket,Client_Address):
        ReverseProxy_SenderSocket=self.Build_Socket()
        Server_IP,Server_Port=LoadBalancer.LoadBalancer.Get_ServerIP(Client_Address)
        ReverseProxy_SenderSocket.connect((Server_IP,Server_Port))
        while True:
            data=Client_Socket.recv(1024)
            ReverseProxy_SenderSocket.sendall(data)
            data=ReverseProxy_SenderSocket.recv(1024)
            Client_Socket.sendall(data)

    def Inizialize_LoadBalancer(self):
        try:
            self.Load_Balancer=LoadBalancer.LoadBalancer()
        except Exception as e:
            print("Error Occured in LoadBalancer Module")
    
    
    def ConnectServerToReverseProxy(self, ServerName, Server_IP, Server_Port):
        try:
            self.Load_Balancer.Map_ServerIP(ServerName,Server_IP,Server_Port)  
        except Exception as e:
            print("Error Occured in LoadBalancer Module")
    
    
    def Build_Socket(self):
        try: 
            Socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            return Socket
        except Exception as e:
            print("Error Occured in Socket library")

