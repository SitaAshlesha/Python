import random       #build-in module
x = random.randrange(1,10)      #method
chance = 1
while chance <= 10:  #condition Statement
    guess_no = int(input("Enter guess number:  \n"))
    if x == guess_no:
        print("You are winner")
        break
    else:
        print("better luck next time ")
        chance += 1