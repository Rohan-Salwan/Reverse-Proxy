from cache import Cache
import unittest


class TestCache(unittest.TestCase):
    def test_CacheAttributes(self):
        CacheInstance=Cache()
        assert CacheInstance.Map == {} and CacheInstance.count == 0

    def test_CacheAttributeHeadTail(self):
        CacheInstance=Cache()
        assert CacheInstance.head == None and CacheInstance.tail == None

    def test_CachePutMethod(self):
        CacheInstance=Cache()
        CacheInstance.Put("key1","value1")
        CacheInstance.Put("key2","value2")
        TestResult=False
        if "key1" in CacheInstance.Map and "key2" in CacheInstance.Map:
            TestResult=True
        assert CacheInstance.head.key == "key1" and CacheInstance.tail.key == "key2" and TestResult==True
    
    def test_CacheEvictionPolicy(self):
        CacheInstance=Cache()
        i=1
        while i<102:
            CacheInstance.Put("key"+str(i),"value"+str(i))
            i+=1
        assert "key1" not in CacheInstance.Map and CacheInstance.head.key != "key1"

    def test_CacheGetMethodSimpleAndOveridingVersion(self):
        CacheInstance=Cache()
        CacheInstance.Put("key1","value1")
        CacheInstance.Put("key2","value2")
        TestResult1=CacheInstance.get("key1")
        CacheInstance.get("key2",Update_Node="Newvalue")
        TestResult2=CacheInstance.get("key2")
        assert TestResult1=="value1" and TestResult2=="Newvalue"

    def test_CacheDelete(self):
        CacheInstance=Cache()
        CacheInstance.Put("key1","value1")
        CacheInstance.Put("key2","value2")
        CacheInstance.delete("key2")
        assert "key2" not in CacheInstance.Map
        

    
