#! python3
import time, sys

def delay_print(s):
    for l in s:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.05)

secret_word = 'main'

delay_print('Hello Akshay, here is a game where you can guess a ' + str(len(secret_word)) +' letter word! \nYou have 9 attempts, you can change the word afterwards.\n')

guess=''
guess_count= 0 # variable that is iterated by 1
guess_limit= 9 # number of guesses

while guess != secret_word:
    if guess_count == guess_limit:
        delay_print('\nYou do not win! Better luck next time old pal, the word was '+ secret_word+'\n')
        break
    guess = input('Enter guess: ')
    guess_count += 1
    if guess == secret_word:
        print('You have broken the cycle!') # exits the loop
    else:
        more_guess = guess_limit - guess_count
        print('Not quite! You have '+str(more_guess)+' more guesses!')
