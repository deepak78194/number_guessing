import random
import datetime as dt
import time
print("** Welcome to guessing game, Lets Challenge me ** \n")

date_now = dt.date.today()
t = time.localtime()
time_now = time.strftime("%H:%M:%S", t)
print(f"Today Date: {date_now}", end="\t\t")
print(f"Current Time: {time_now}\n")

player_name = str(input("Enter your name: "))

guess_start_limit = int(input("\nEnter a guessing starting limit:  "))
guess_end_limit  = int(input("Enter a guessing ending limit: "))

guess_number = int(input( f"\n\nEnter the number to computer guess between {guess_start_limit} to {guess_end_limit}: "))

print("\nLets start the Game.........!! \n")

print("Note: \n   1. if computer guess is low then enter (l,L,low,LOW)\n   "
      "2. if computer guess is high the enter (h,H,high,HIGH)\n   "
      "3. if it guess correctly enter (c,C,correct,CORRECT)\n\n")

while True:
    computer_guess = random.randint(guess_start_limit,guess_end_limit)

    result = input(f"{player_name}, {computer_guess} is correct or low or high: ")

    if result in ['l', 'L', 'low', 'LOW']:
        guess_start_limit = computer_guess + 1
        continue
    elif result in ['h', 'H', 'high', 'HIGH']:
        guess_end_limit = computer_guess - 1
        continue
    elif result in ['c', 'C', 'correct', 'CORRECT']:
        print(f"\n\nHey {player_name} see me, I am done.. ")
        print("Haha..I am smarter then you right !!")
        break
