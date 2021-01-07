import datetime as dt
import time
import random
print("\t!...Welcome to guessing game...!\n\n")


date_now = dt.date.today()
t = time.localtime()
time_now = time.strftime("%H:%M:%S", t)
print(f"Today Date: {date_now}", end="\t\t")
print(f"Current Time: {time_now}\n")

player_name = str(input("Enter your name:" ))

guess_limit = int(input("Please enter the guessing limit: "))

guess_value = random.randint(0,guess_limit)
print("........Lets start the guessing game.......")


while True:

    value = int(input("enter the number: "))

    if value < guess_value:
        print("Sorry, Guess again. Number is too low")
        print("-------------------------------------------------------------------------------")

    elif value > guess_value:
        print("Sorry, Guess again. Number is too high")
        print("-------------------------------------------------------------------------------")

    elif value == guess_value:
        print("...........Great guessing.............")
        result = f"Congratulations {player_name}, you guess the number correctly...."
        print(result)
        break




