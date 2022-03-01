def test(string):
    
    vowels='aeiou'
    if string[0] in vowels:  #clave
        return f'{string}way'
        
    else:
        return f'{string[1:]}{string[0]}ay' #slices
        
def separador(string):
         
         phrase=[]
         
         for i in string.split(): #iterable puede usar method
             phrase.append(test(i)) #el argumento del append llamar a una funcion, el resultado anexarlo
             
         phrase=" ".join(phrase)
         return phrase
         
         
def run():
    sentence=input('Enter a phrase: ')
    print(separador(sentence))
    
    
    
        

if __name__== '__main__':
   run()

#Book's solution

# def pl_sentence(sentence):
#     output = []
#     for word in sentence.split():
#         if word[0] in 'aeiou':
#             output.append(f'{word}way')
#         else:
#             output.append(f'{word[1:]}{word[0]}ay')
 
#     return ' '.join(output)
 
# print(pl_sentence('this is a test'))