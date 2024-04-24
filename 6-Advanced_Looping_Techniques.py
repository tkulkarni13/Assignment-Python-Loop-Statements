# Task 1: The Selective DJ

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
for g in genres[2:4]:
    print(g)

# Task 2: The One-Liner Band with List Comprehensions

new_genres = [g + " Music" for g in genres]
print(new_genres)

# Task 3: Numerical Beats with range

for i in range(10, 0, -1): # prints descending numbers from 10 -> 1
    print(i)
print("The beat drops now!")