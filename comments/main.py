# Do not modify these lines
__winc_id__ = '63ce21059cf34d3d8ffef497ede7e317'
__human_name__ = 'comments'

# Add your code after this line
import random
#initialize guess and lives, set a random number between 1 - 10, 
random_number = random.randint(1, 10)
guess =  None
lives = 3
#while the random number is not guessed, perform if else statement.
while guess != random_number and lives > 0:
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)

#if the number is guessed correctly, show message + guessed number
    if random_number == guess:
        print("You successfully guessed the number: ", random_number)  
#else print a try again message
    else:
       lives = lives - 1
       result = f"You guessed wrong! You have: {lives} lives left!"
       print(result)