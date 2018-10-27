# enough_sleep.py
user_sleep = input("How much did you sleep last night?\n>")
user_sleep = int(user_sleep)
if user_sleep <=6:
    print("You failed! you have insomnia!")
if user_sleep >=10:
    print("You are sleeping too much")
if user_sleep <10 and user_sleep > 6:
    print("Takin care of yourself. Good job!")
