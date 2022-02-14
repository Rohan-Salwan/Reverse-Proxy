import LoadBalancer
import logging
from cache import Cache
from bs4 import BeautifulSoup


logger=logging
logger.basicConfig(filename="Logs.txt",level=logging.DEBUG,format = '%(asctime)s %(levelname)s %(name)s %(message)s')


def Inizialize_LoadBalancer(test=False):
    try:
        if test:
            replicas=4
            Load_Balancer=LoadBalancer.LoadBalancer(replicas)
            ServerName="Server1"
            Server_IP="192.168.1.1"
            Server_Port="8000"
        else:
            print("please provide server replicas for load balancer")
            replicas=RetrieveInputFromUser(type=int)
            Load_Balancer=LoadBalancer.LoadBalancer(replicas)
            print("Please Provide ServerName below")
            ServerName=RetrieveInputFromUser()
            print("Please Provide Server_IP below")
            Server_IP=RetrieveInputFromUser()
            print("Please Provide Server_Port below")
            Server_Port=RetrieveInputFromUser(type=int)
        Load_Balancer.Map_ServerIP(ServerName,Server_IP,Server_Port)
        return Load_Balancer
    except Exception as e:
        print("Error Occured in LoadBalancer Module")
        logger.debug(e)

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
            User_Input=type(input())
            return User_Input
        except Exception as e:
            print("Invalid Input")

def Initialize_Cache():
    try:
        cache=Cache()
        return cache
    except Exception as e:
        print("Error Occured in Cache Module")
        logger.debug(e)
