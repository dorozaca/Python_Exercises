import unittest

def ub_func(string):
    
    counter=[ ]
    for index, letra  in enumerate(string):
        
        if letra in 'aeiou':
            counter.append(index)
    
    counter.sort(reverse=True)
      
    for i in counter:
          new_word=f'{string[:i]}ub{string[i:]}'
          string=new_word
    return new_word
        
class Mytest(unittest.TestCase):
   def test_ub(self):
        word='elephant'
        prueba=ub_func(word)
        self.assertEqual(prueba,'ubelubephubant')
    

def run():
    word=input('Enter the word :')
    print(ub_func(word))
    
if __name__== '__ffmain__':
    unittest.main()
    run()

#pendiente revisar book's solution
    