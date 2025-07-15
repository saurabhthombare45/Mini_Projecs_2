import random
n=random.randint(1,100)
# print(f"The Guess Wold be {n}")
a=-1
guesses = 0
while (a != n):
    a=int(input("Guess a Number:-"))
    if a==n:
        break
    else:

        if a>n:
            print("Lower Number plz")
        else:
            print("Higher Number plz")
    guesses +=1

# print(f"You Guessed the number in {guesses} attempts")
if(guesses == 1):
    print("You are the CHAMPION you guessed it in One Time")
else:
    print(f"You Guessed the {n} Number in {guesses} attempts")

            
