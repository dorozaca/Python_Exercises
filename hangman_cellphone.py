import random


def run():
    prueba=['violeta','lily','toto','dakota']
    target=list(random.choice(prueba))
   
    
    print('Guess the word:')
    Blanks=list((len(target)*'-'))
    print("".join(Blanks))
        
    
    counter=0
    tries=3
    
    while Blanks != target:
            if tries!=0:
                guess=input('Enter letter: ')
                for index, palabra in enumerate(target):
                
                    if guess==palabra:
                        Blanks[index]=guess
                        counter +=1 #each time user gets right guess counter increases 
                        
                    
                        
                if counter<1:    #if after looping through user didn't get any right guess counter==0
                    tries -=1    #which means we need to subtract one try
                counter=0        #and reset counter for bext try
            else:
                print('You lost!') #if tries are reduced to zero
                break              #game is over and while loop ends
                
                
            print("".join(Blanks))
            print()
 
    if Blanks == target: #however loop can end too because this condition. This is final validation of it
        print('You won!')
    
if __name__== '__main__':
    run()