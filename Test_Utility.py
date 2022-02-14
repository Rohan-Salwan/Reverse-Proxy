import unittest
import Utility
from LoadBalancer import LoadBalancer
from bs4 import BeautifulSoup
from unittest.mock import patch
from cache import Cache

class TestUtulity(unittest.TestCase):
    
    def test_InitializeLoadBalancer(self):
        TestingInstance=Utility.Inizialize_LoadBalancer(test=True)
        self.assertIsInstance(TestingInstance,LoadBalancer)

    def test_InitializeLoadBalancerMapServerInnerMethod(self):
        ServerName="Server1"
        Server_IP="192.168.1.1"
        Server_Port="8000"
        LoadBalancerInstance=LoadBalancer(4)
        LoadBalancerInstance.Map_ServerIP(ServerName,Server_IP,Server_Port)
        TestingInstance=Utility.Inizialize_LoadBalancer(test=True)
        self.assertEqual(TestingInstance.Server_Ids,LoadBalancerInstance.Server_Ids)

    def test_InitializeLoadBalancerMapServerReplicas(self):
        ServerName="Server1"
        Server_IP="192.168.1.1"
        Server_Port="8000"
        LoadBalancerInstance=LoadBalancer(4)
        LoadBalancerInstance.Map_ServerIP(ServerName,Server_IP,Server_Port)
        TestingInstance=Utility.Inizialize_LoadBalancer(test=True)
        self.assertEqual(TestingInstance.Server_Replicas,LoadBalancerInstance.Server_Replicas)

    def test_LinkParser(self):
        html="<a href='https://www.w3schools.com/'>Visit W3Schools.com!</a>"
        object=BeautifulSoup(html,"lxml")
        TestResult=Utility.LinksParser(object)
        TestResult=TestResult.decode()
        if "localhost" in TestResult:
            TestResult=True
        self.assertTrue(TestResult)

    def test_ImageParser(self):
        html="<img src='https://www.w3schools.com/'>Visit W3Schools.com!>"
        object=BeautifulSoup(html,"lxml")
        TestResult=Utility.ImageParser(object)
        TestResult=TestResult.decode()
        if "localhost" in TestResult:
            TestResult=True
        self.assertTrue(TestResult)

    def test_PrimaryParser(self):
        html="<img src='https://www.w3schools.com/'>Visit W3Schools.com!><a href='https://www.w3schools.com/'>Visit W3Schools.com!</a>"
        object=BeautifulSoup(html,"lxml")
        TestResult=Utility.Primary_Parser(object)
        TestResult=TestResult.decode()
        if "localhost" in TestResult:
            TestResult=True
        self.assertTrue(TestResult)
        
    def test_retrieveInputFromUser(self):
        with patch('Utility.RetrieveInputFromUser') as RetrieveInputFromUser:
           RetrieveInputFromUser.return_value = None
        self.assertIsNone(RetrieveInputFromUser())
    
    def test_InitializeCache(self):
        cache=Utility.Initialize_Cache()
        self.assertIsInstance(cache,Cache)
