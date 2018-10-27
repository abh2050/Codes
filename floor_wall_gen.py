# floor_wall_gen.py
import random
floor_wall_list = ['_', '|']
out_string = ''
out_string = out_string + random.choice(floor_wall_list)
out_string = out_string + random.choice(floor_wall_list)
out_string = out_string + random.choice(floor_wall_list)
out_string = out_string + random.choice(floor_wall_list)
print(out_string)
