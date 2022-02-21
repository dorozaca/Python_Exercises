# cities=['Lima', 'Rio', 'Buenos Aires', 'Santiago', 'Quito']
# enum=list(enumerate(cities,2))
# print(enum)

################################# MI SOLUCION ###############################################

# import random

# def guessing_name():
#     objective=random.randint(0,100)
#     print(objective)
#     guessed_number=int(input('Please enter number: '))

#     while guessed_number!=objective:
#         if guessed_number>objective:
#             print('Too High')
#             guessed_number=int(input('Please enter number: '))

#         else:
#             print('Too low')
#             guessed_number=int(input('Please enter number: '))

#     print('Just right')

# def run():
#     guessing_name()

# if __name__== '__main__':
#     run()

################################# BOOK'S SOLUTION ###############################################
import random

def guessing_game():
    answer = random.randint(0, 100)
    
    counter=1

    while counter<10:
        user_guess = int(input('What is your guess Izzy crazy? '))
        if user_guess == answer:
            print(f'Right! The answer is {user_guess}')
            break
        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')
            counter +=1
        else:
            print(f'Your guess of {user_guess} is too high!')
            counter +=1

    print('You didn\'t guess in time')
    

def run():
    guessing_game()

if __name__== '__main__':
    run() 