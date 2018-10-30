#rand_emo.py
import random
eye_list = [':',';']
nose_list = ['~','@','^']
mouth_list = ['o','O','OO']
out_string = ''
out_string = out_string + random.choice(eye_list)
out_string = out_string + random.choice(nose_list)
out_string = out_string + random.choice(mouth_list)
print(out_string)
