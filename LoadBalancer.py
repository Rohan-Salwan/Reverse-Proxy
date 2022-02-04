import bisect

class LoadBalancer:
    def __init__(self, Replicas):
        self.Server_Replicas=Replicas
        self.Server_Ids = []
        self.Server_Map = {}

    def Hash_Value(self,key):
        hash_value = key%360
        return hash_value

    def Map_ServerIP(self,Server_Name,Server_IP):
        for Replica in range(self.Server_Replicas):
            Server_Name=Server_Name+str(Replica)
            Ascii_Value = self.Ascii(Server_Name)
            Hash_Key = self.Hash_Value(Ascii_Value)
            print(Hash_Key)
            self.Server_Map[Hash_Key]=Server_IP
            bisect.insort(self.Server_Ids, Hash_Key)
    
    def Get_ServerIP(self, request):
        Ascii_Value=self.Ascii(request)
        Hash_Key = self.Hash_Value(Ascii_Value)
        Index=bisect.bisect(self.Server_Ids,Hash_Key)
        if Index==len(self.Server_Ids):
            Index=0
        ServerIP_Key=self.Server_Ids[Index]
        ServerIP=self.Server_Map[ServerIP_Key]
        return ServerIP
    
    def Delete_ServerIP(self,Server_Name):
        for Replica in range(self.Server_Replicas):
            Server_Name=Server_Name+str(Replica)
            Ascii_Value=self.Ascii(Server_Name)
            Hash_Key=self.Hash_Value(Ascii_Value)
            try:
                self.Server_Map.pop(Hash_Key,None)
                self.Server_Ids.remove(Hash_Key)
            except Exception as e:
                print("ServerIP is Invalid")    
    
    def Ascii(self,string):
        value=0
        for char in string:
            value+=ord(char)
        return value