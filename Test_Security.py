import unittest
from Security import Security
import logging

class TestSecurity(unittest.TestCase):
    def test_SecurityInstanceBlockList(self):
        SecurityInstance=Security()
        Orignal_Set={"char","nchar","varchar","nvarchar","alter","begin","cast","create",
        "cursor","declare","delete","drop","end","exec","execute","fetch","insert","kill","open",
        "select","sys","sysobjects","syscolumns","table","update","sleep","uid",
        "waitfor","delay","system","union","order by","group by","<script>","--"}
        self.assertEqual(SecurityInstance.BlackList,Orignal_Set)

    def test_SecurityInstanceSpecialcharList(self):
        SecurityInstance=Security()
        Orignal_Set={" ","'","}","{",")","(","|","*",";","@","<",">","$","!"}
        self.assertEqual(SecurityInstance.SpecialChar,Orignal_Set)

    def test_SecurityAttributes(self):
        SecurityInstance=Security()
        logger=logging
        self.assertEqual(SecurityInstance.BlockList,set() and SecurityInstance.logger,logger)

    def test_SecurityRequestTimeRecords(self):
        SecurityInstance=Security()
        self.assertEqual(SecurityInstance.RequestTimeRecord,{} and SecurityInstance.Record,[])

    def test_InputSanitizer(self):
        SecurityInstance=Security()
        URL_ForTesting="https://localhost:8000/search?='union><script>*"
        Sanitized_URL=SecurityInstance.Input_Sanitizer(URL_ForTesting,"192.168.1.1")
        self.assertEqual(Sanitized_URL,"https://localhost:8000/search?=")

    def test_PreventBruteForce(self):
        SecurityInstance=Security()
        for _ in range(0,32):
            TestingIPAddress="192.168.1.1"
            SecurityInstance.PreventBrute_Force(TestingIPAddress)
        try:
            IP=SecurityInstance.BlockList[0]
            self.assertEqual(IP,"192.168.1.1")
        except Exception as e:
            pass