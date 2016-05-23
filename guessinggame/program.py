import random

print()
print()
print('-----------------------------------------')
print('-------- Guess the number game ----------')
print('-----------------------------------------')
print()

the_number = random.randint(0,100)
guess = -9999

while guess != the_number:
        
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('too low')
    elif guess > the_number:
        print('too high')
    else:
        print('the number was: ' + str(the_number))
        print('you win!')
