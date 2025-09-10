import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#randomly picking values from Lists
random_friends=random.choice(friends)
print(random_friends)
random_pick= random.randint(0,4)
print(friends[random_pick])
