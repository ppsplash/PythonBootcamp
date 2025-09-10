import random

import my_module
#random_int=random.randint(1,10) #to print random integers  between & inclusive 1 and 10
#print(random_int)
#random_no_0_to_1= random.random()*10 # to print random numbers 0.0 to 1.0 -- in which 0 will be inclusive and 1 will not be included
#print(random)
#random_decimal =random.uniform(1,10) # to print floating numbers in which a and b are inclusive
#print(random_decimal)
#print(my_module.my_fav_no) # to print variable from another module/file
random_heads_or_tail= random.randint(0,1)
if random_heads_or_tail == 0 :
    print("Heads")
else:
    print("Tails")




