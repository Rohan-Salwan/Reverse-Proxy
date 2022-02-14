import unittest
from LoadBalancer import LoadBalancer

class TestLoadBalancer(unittest.TestCase):
    
    def test_MapServerIP(self):
        LoadBalancerInstance=LoadBalancer(4)
        TestIP="192.168.1.1"
        TestName="Server1"
        TestPort=8000
        LoadBalancerInstance.Map_ServerIP(TestName,TestIP,TestPort)
        self.assertNotEqual(LoadBalancerInstance.Server_Ids,[] and LoadBalancerInstance.Server_Map,{})

    def test_SortingOrderofServerID(self):
        LoadBalancerInstance=LoadBalancer(4)
        TestIP="192.168.1.1"
        TestName="Server1"
        TestPort=8000
        LoadBalancerInstance.Map_ServerIP(TestName,TestIP,TestPort)
        CustomizeSortedList=sorted(LoadBalancerInstance.Server_Ids)
        self.assertEqual(LoadBalancerInstance.Server_Ids,CustomizeSortedList)

    def test_GetServerIP(self):
        LoadBalancerInstance=LoadBalancer(4)
        TestIP="192.168.1.1"
        TestName="Server1"
        TestPort=8000
        LoadBalancerInstance.Map_ServerIP(TestName,TestIP,TestPort)
        Client_Request="192.168.1.2"
        ServerIPForNewRequest=LoadBalancerInstance.Get_ServerIP(Client_Request)
        IP,Port=ServerIPForNewRequest[0],ServerIPForNewRequest[1]
        self.assertTrue(str(IP) and int(Port))
    
    def test_DeleteServerIP(self):
        LoadBalancerInstance=LoadBalancer(4)
        TestIP="192.168.1.1"
        TestName="Server1"
        TestPort=8000
        LoadBalancerInstance.Map_ServerIP(TestName,TestIP,TestPort)
        LoadBalancerInstance.Delete_ServerIP("Server1")
        self.assertEqual(LoadBalancerInstance.Server_Ids,[] and LoadBalancerInstance.Server_Map,{})

    def test_Ascii(self):
        String="Server1"
        value=0
        for char in String:
            value+=ord(char)
        AsciiValue=LoadBalancer.Ascii(LoadBalancer,String)
        self.assertEqual(AsciiValue,value)

    def test_LoadBalancerReplicas(self):
        LoadBalancerInstance=LoadBalancer(4)
        self.assertEqual(LoadBalancerInstance.Server_Replicas,4)

    def test_LoadBalancerAttributes(self):
        LoadBalancerInstance=LoadBalancer(4)
        self.assertEqual(LoadBalancerInstance.Server_Ids,[] and LoadBalancerInstance.Server_Map,{})
 
    def test_HashValue(self):
        Hash_Value=LoadBalancer.Hash_Value(LoadBalancer,200)
        Fake_Value=200%360
        self.assertEqual(Fake_Value,Hash_Value)
