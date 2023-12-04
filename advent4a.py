# Amy Bakaletz - 2023

# read in the data file
file = open("advent4.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

total = 0
for i in range(len(data)):
    points = 0

    # load winning numbers
    colon = data[i].find(":")
    bar = data[i].find("|")
    # learned to do enumeration to cast to ints
    winners = [int(x) for x in data[i][colon+2:bar].split()]

    # load your hand
    hand = [int(x) for x in data[i][bar+1:].split()]

    # traverse your numbers and count winning
    # +1 for first, *2 for all others
    for j in range(len(hand)):
        if(hand[j] in winners):
            if(points == 0):
                points = 1
            else:
                points *=2

    # add to total
    total += points

print(total)
