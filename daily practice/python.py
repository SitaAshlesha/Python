import random
guess_number = random.randint(1,10)
attempts = 0
print("welcome to number guessing game")
while True:
    try:
       guess = int(input("Guess your number"))
       attempts += 1
       if guess == guess_number:
           print("your guess is correct")
           break
       else :
       print("again")
