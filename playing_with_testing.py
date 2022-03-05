import unittest

def mi_suma(x,y):
    return x+y

class testing(unittest.TestCase):
    def test_suma(self):
        a=10
        b=5
        solution=mi_suma(a,b)
        self.assertEqual(solution,15)

if __name__ =='__main__':
    unittest.main() #no olvidar parentesis

    

    