import random

# Task 1: Your mood tracker

moods = ["happy", "sad", "energetic", "calm"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_of_day = ["morning", "afternoon", "evening"]
for day in range(7):
    for time in range(3):
        print("On " + days[day] + " " + time_of_day[time] + ", you were feeling " + random.choice(moods) + ".")