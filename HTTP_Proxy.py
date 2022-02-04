import socket
import threading
import logging

class HTTP_Proxy:
    def __init__(self):
        Server_Adderess=""
        Server_Port = int(input("Please provide port"))
        ProxyServer_Socket=self.Build_Socket()
        ProxyServer_Socket.bind((Server_Adderess,Server_Port))
        ProxyServer_Socket.listen(5)
        self.Main(ProxyServer_Socket)

    def Main(self,ProxyServer_Socket):
        while True:
            Client_Socket, Client_Address=ProxyServer_Socket.accept()
            Thread=threading.Thread(target=self.MiddleManProcess,args=(Client_Socket,Client_Address))
            Thread.start()
                
    def MiddleManProcess(self,Client):
        Proxy_Client=self.Build_Socket()
        while True:
            dataa=Client.recv(8192)
            if len(dataa)>0:
                data=dataa.decode("utf-8")
                addr,port=self.Parsing_WebAddress(data)
                print(addr,port)
                Proxy_Client.connect((addr,port))
                Proxy_Client.sendall(dataa)
                Server_Response=Proxy_Client.recv(8192)
                Client.sendall(Server_Response)

    def Parsing_WebAddress(self,data):
        first_line=data.split("\n")[0]
        url=first_line.split(" ")[1]
        http_pos=url.find("://")
        if http_pos == -1:
            temp=url
        else:
            temp=url[(http_pos+3):]
        port_pos=temp.find(":")
        webserver_pos=temp.find("/")
        if webserver_pos==-1:
            webserver_pos=len(temp)
        webserver=""
        port = -1
        if port_pos==-1 or webserver_pos<port_pos:
            port=80
            webserver=temp[:webserver_pos]
        else:
            port=int(temp[(port_pos+1):][:webserver_pos-port_pos-1])
            webserver=temp[:port_pos]
        return webserver,port


    def Build_Socket(self):
        try: 
            Socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            return Socket
        except Exception as e:
            print("Error Occured in Socket library")