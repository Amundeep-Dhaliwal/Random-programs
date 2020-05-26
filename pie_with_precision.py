#!python3

'''
Find e to the Nth digit
enter a number and have the program generate e to that many decimal places
'''

import math

def e_with_precision(n):
    '''
    return euler's number to the nn th decimal place
    enter and integer
    return type string
    '''
    return f'{math.e:.{n}f}'

def pi_with_precision(n):
    '''
    return pi to the nn th decimal place
    enter and integer
    return type string
    '''
    return f'{math.pi:.{n}f}'




print('Welcome to a script that determines a precise value for pi and euler\'s number.')

super_true = True
while super_true:
    true_bool = True
    while true_bool:
        try:
            precision = int(input('Please enter the required number of decimal places for pi (1-50): '))
        except ValueError:
            print('Sorry please enter a number between 1 and 50')
            continue
        if 51 <= precision or precision < 1:
            print('Sorry please enter a number between 1 and 50')
            continue
        else:
            true_bool= False
    print(f'pi: {pi_with_precision(precision)}')



    true_bool = True
    while true_bool:
        try:
            precision = int(input('Please enter the required number of decimal places for euler\'s number (1-50): '))
        except ValueError:
            print('Sorry please enter a number between 1 and 50')
            continue
        if 51 <= precision or precision < 1:
            print('Sorry please enter a number between 1 and 50')
            continue
        else:
            true_bool= False
    print(f'Euler\'s number: {e_with_precision(precision)}')

    if input('Do you want to try again? (y/n) ').lower().startswith('y'):
        continue
    else:
        print('Thank you for your time.')
        break
