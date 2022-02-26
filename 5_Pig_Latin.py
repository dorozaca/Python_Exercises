# def pig_latin(string):
    
#     string=list(string)
#     vowels=['a','e','i','o','u']
#     when_vow='way'
#     cons='ay'

#     for i in vowels:
#         if i == string[0]:
#             string.append(when_vow)
            
        
#     length=len(string)        
#     if string[length-1] != 'way':
    
#         counter=0
        
#         reserved_word=string[0] 

#         while counter<length-1:
#             string[counter]=string[counter+1]
#             counter+=1

        
#         string[length-1]=reserved_word
#         string.append(cons)
    
#     string="".join(string)
#     print(string)

            



# def run():
#     string=input('Add the word you want to translate into pig latin language: ')
#     pig_latin(string)

# if __name__== '__main__':
#     run()

def pig_latin(string):
    vowels=['a','e ','i','o','u']

    if string[0] in vowels:
        return f'{string}way'

    else:
        return f'{string[1:]}ay'


def run():
    word=input('Enter a word: ')
    print(pig_latin(word))

if __name__=='__main__':
    run()