#grade.py
user_input = input("what grade did you get?\n>")
user_input = int(user_input)
if user_input <=100 and user_input >=90:
    print("A")
if user_input <=89 and user_input >=80:
    print("B")
if user_input <=79 and user_input >=70:
    print("C")
if user_input <=69 and user_input >=60:
    print("D")
if user_input <=59 and user_input >=0:
    print("F")
