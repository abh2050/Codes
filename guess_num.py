#guess_num.py
import random
num1 = random.randint(1,10)
user_input = input(f"what is the number?>")
user_input = int(user_input)
while True:
    if user_input == num1:
        print("corret")
        break
    elif user_input > num1:
        print("too high")
    elif user_input <num1:
        print("too low")
    user_input = input(f"what is the number>")
    user_input = int(user_input)
