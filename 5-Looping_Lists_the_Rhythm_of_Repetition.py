# Task 1: The for Loop DJ Set

genres = ['Jazz', 'Rock', 'Hip-Hop', 'Classical']

for g in genres:
    if (g == genres[0]):
        print("Jazz music jazzes up my soul.")
    if (g == genres[1]):
        print("Rock music makes me rock my body.")
    if (g  == genres[2]):
        print("Hip-Hop forces me hop to the beat.")
    if (g == genres[3]):
        print("Classical music makes me feel classy.")

# Task 2: The Remix Artist with while

i = 0
while i < 4:
    if (i == 0):
        print(genres[i] + " music jazzes up my soul.")
    if (i == 1):
        print(genres[i] + " music makes me rock my body.")
    if (i ==2):
        print(genres[i] + " forces me hop to the beat.")
    if (i ==3):
        print(genres[i] + " music makes me feel classy.")
    i += 1

# Task 3: Light Show Technician Loop

for i in range(4):
    if (genres[i] == 'Rock' or genres[i] == 'Hip-Hop'):
        print(genres[i] + " is ready for the light show.")
    #else:
        #print(genres[i] + " will not have a light show.")