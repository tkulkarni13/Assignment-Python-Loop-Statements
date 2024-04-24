import random

# Task 1: Your mood today

moods = ["happy", "sad", "energetic", "calm"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in range(7):
    print("On " + days[day] + ", you were feeling " + random.choice(moods) + ".")