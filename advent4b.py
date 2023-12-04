# Amy Bakaletz - 2023

# read in the data file
file = open("advent4.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

cards = []
# make a list of cards to keep up with how many you have of each card
for i in range(len(data)):
    space = data[i].find(" ")
    colon = data[i].find(":")
    cards.append([int(data[i][space +1:colon]),1])

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
            points +=1

    # duplicate cards
    j = i + 1
    while(j < i + points + 1 and j < len(cards)):
        cards[j][1] += cards[i][1]
        j += 1

total = 0
for i in range(len(cards)):
    total += cards[i][1]
print(total)
