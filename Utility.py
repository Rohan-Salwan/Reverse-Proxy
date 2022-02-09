import LoadBalancer
import logging
from cache import Cache



def Inizialize_LoadBalancer():
    try:
        Load_Balancer=LoadBalancer.LoadBalancer()
        return Load_Balancer
    except Exception as e:
        print("Error Occured in LoadBalancer Module")

def ConnectServerToReverseProxy(Load_Balancer):
    print("Please Provide ServerName below")
    ServerName=RetrieveInputFromUser()
    print("Please Provide Server_IP below")
    Server_IP=RetrieveInputFromUser()
    print("Please Provide Server_Port below")
    Server_Port=RetrieveInputFromUser(type=int)
    try:
        return Load_Balancer.Map_ServerIP(ServerName,Server_IP,Server_Port)  
    except Exception as e:
        print("Error Occured in LoadBalancer Module")


def Primary_Parser(response):
        response=LinksParser(response)
        response=ImageParser(response)
        return response
    
def LinksParser(response):
    for link in response.find_all('a'):
        hyperlink=link["href"]
        link["href"]="http://localhost:8080/"+hyperlink
    return response

def ImageParser(response):
    for image in response.find_all('img'):
        Imagelink=image['src']
        image['src']="http://localhost:8080/"+Imagelink
    return response

def RetrieveInputFromUser(type=str):
    while True:
        try:
            User_Input=type(input("Please Provide Server Name"))
            return User_Input
        except Exception as e:
            print("Invalid Input")

def Initialize_Cache():
    try:
        cache=Cache()
        return cache
    except Exception as e:
        print("Error Occured in Cache Module")
