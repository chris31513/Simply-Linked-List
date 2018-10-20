import unittest
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from src.List import List
    else:
        from ..src.List import List
        
class TestList(unittest.TestCase):
    
    def test_add(self):
        list = List()
        list.add("hola")
        self.assertTrue(list.get_head().get_elem() == "hola")
        
    def test_remove(self):
        list = List()
        list.add("hola")
        list.add("adios")
        list.remove("hola")
        self.assertEquals(list.get_head().get_elem(),"adios")

    def test_contains(self):
        list = List()
        list.add("hola")
        list.add("adios")
        self.assertTrue(list.contains("adios"))
    
    def test_get_node(self):
        list = List()
        list.add("hola")
        self.assertTrue(list.get_node("hola") != None)

    def test_is_head(self):
        list = List()
        for i in range(0,10):
            list.add(i)
        self.assertTrue(list.is_head(list.get_node(0)))

    def test_is_tail(self):
        list = List()
        for i in range(0,101):
            list.add(i)
        self.assertTrue(list.is_tail(list.get_node(100)))

    def test_to_string(self):
        list = List()
        for i in range(0, 10):
            list.add(i)
        self.assertEquals(list.to_string(),"[0,1,2,3,4,5,6,7,8,9]")
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestList)
    unittest.TextTestRunner(verbosity=2).run(suite)
