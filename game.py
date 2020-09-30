import random #Choose random number 
"""A number-guessing game."""
print ("Welcome To Guess The Number Game!") #Player greeting 
answer =input("Enter your name: ") #Get player name
print(answer+ ", I'm thinking of a number between 1 and 100")
number =random.randint(1,100)

num = int (input("Try to guess my number: "))
guess_attempts= 0

while number != num: 
    if number < num: 
        print ("your guess is too high, try again." )
        num = int(input("your guess? " ))
        guess_attempts += 1 #equivalent to guess_attempts= guess_attempts + 1
    elif num < number: 
        print ("your guess is too low, try again." ) 
        num = int(input("your guess? " ))
        guess_attempts += 1
else:
    guess_attempts += 1
    string_guess_attempts= str(guess_attempts)
    print ("Well done, "+answer+"! You found my number in "+string_guess_attempts+" tries!")        
  
        

             









