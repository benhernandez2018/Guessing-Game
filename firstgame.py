# Guessing game to guess number
import random

#the whole game can be called with the function guessingGame()

def guessingGame():

    #introduce the player to the game
    print('Welcome to the game!')

    #create the number and store it

     #creates the secret number
    #secretNumber = 35 for debuggind purpose
    secretNumber = random.randint(1,100)
    print("I'm thinking of a number between 1 and 100")

    
    #main function of the game(while loop)
   
    while True:

    #asks the user to guess the number
        guess = int(input('Guess the number! '))

        if guess == secretNumber:
            print('You found it!')
            break
        elif guess > secretNumber:
            print('Guess a lower number')
            continue
        else:
            print('Guess a higher number')
            continue

    
    #ask user to play again or end the game
    play_again = input('Would you like to play again? (y/n)').lower()

    while True: #ask until the user puts correct input

        if play_again == 'y':
            return guessingGame()
        elif play_again == 'n':
            print('Goodbye! Play again soon.')
            quit()
        else:
            print('Error, Try again')
            continue

guessingGame()

        


        
            