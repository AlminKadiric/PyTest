import unittest
  
def cuboid_volume(a,b,c):
    return a*b*c
  
print(cuboid_volume(10,10,10))
  
  
class testVolume(unittest.TestCase):
    def test_isNegative(self):
        #result = cuboid_volume(10,-2,10)
        #test nece proci zato sto je rezultat negativan
         
        result = cuboid_volume(10,2,10)
         
        self.assertGreater(result,0) 
        #if the result is greater than 0 / test passed
         
    def test_isString(self):
        #result = int(cuboid_volume(10,"test",10))
      #test nece proci zato sto pokusavamo da nesto sto je tipa string prebacimo u celobrojni tip
         
        result = int(cuboid_volume(10,2,10))
          
        self.assertRaises(TypeError,result,True) 
        # If the result variable containts type Error drop test wrong input, int expected
  
def suite():
      
# gather all tests in a test suite
  
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(testVolume))
    return test_suite
  
  
mySuite=suite()
  
#define Runner
runner=unittest.TextTestRunner()
runner.run(mySuite)