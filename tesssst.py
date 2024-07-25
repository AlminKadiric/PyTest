import unittest

class firsttest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Create application context")
    
    @classmethod
    def tearDownClass(cls):
        print("Destroy application context")
    
    def setUp(self):
        print("Open db connection")
    def tearDown(self):
        print("Close db connection")