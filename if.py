#!/usr/bin/python
# Filename : if.py

num = 23
guess = int(raw_input('enter an integer: '))

if guess == num:
     print 'Congratulations, you guessed it.' # New block starts here
     print "(but you do not win any prizes!)" # New block ends here
elif guess < num:
     print 'No, it is a little higher than that' # Another block
     # You can do whatever you want in a block ...
else:
    print 'No, it is a little lower than that' 
    # you must have guess > number to reach here

print 'Done'
# This last statement is always executed, after the if statement is executed
