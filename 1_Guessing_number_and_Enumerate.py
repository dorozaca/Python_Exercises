# cities=['Lima', 'Rio', 'Buenos Aires', 'Santiago', 'Quito']
# enum=list(enumerate(cities,2))
# print(enum)

import random

def guessing_name():
    objective=random.randint(0,100)
    print(objective)
    guessed_number=int(input('Please enter number: '))

    while guessed_number!=objective:
        if guessed_number>objective:
            print('Too High')
            guessed_number=int(input('Please enter number: '))

        else:
            print('Too low')
            guessed_number=int(input('Please enter number: '))

    print('Just right')
    
def run():
    guessing_name()

if __name__== '__main__':
    run()
