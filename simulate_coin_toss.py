#! python3
import random
#import pynput
import time
import sys

def delay_print(s):
    for l in s:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.05)

#keyboard = controller()

print('This script simulates a coin toss.')

for i in range(sys.maxsize):
    print('\nPress [ENTER] to simulate a coin toss')
    not_used = input()
    num = random.randint(0,1)
    if num == 1:
        delay_print('Heads\n')
    else:
        delay_print('Tails\n')
