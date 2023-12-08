# read in the data file
file = open("advent7.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

def fiveKind(cards):
    if(cards.count(cards[0]) == 5):
        return True
    else:
        return False

def fourKind(cards):
    if (cards.count(cards[0]) == 4) or (cards.count(cards[1]) == 4):
        return True
    else:
        return False

def fullHouse(cards):
    sorted = []
    for i in range(len(cards)):
        sorted.append(hand[i])
    sorted.sort()
    if(cards.count(sorted[0]) == 2 and cards.count(sorted[4]) == 3) or (cards.count(sorted[0]) == 3 and cards.count(sorted[4]) == 2):
        return True
    else:
        return False

def threeKind(cards):
    if (cards.count(cards[0]) == 3) or (cards.count(cards[1]) == 3) or (cards.count(cards[2]) == 3):
        return True
    else:
        return False

def twoPair(cards):
    sorted = []
    for i in range(len(cards)):
        sorted.append(hand[i])
    sorted.sort()
    if((cards.count(sorted[0]) == 2 and cards.count(sorted[2]) == 2)
            or (cards.count(sorted[0]) == 2 and cards.count(sorted[3]) == 2)
            or (cards.count(sorted[1]) == 2 and cards.count(sorted[3]) == 2)):
        return True
    else:
        return False

def onePair(cards):
    sorted = []
    for i in range(len(cards)):
        sorted.append(hand[i])
    sorted.sort()
    if (sorted[0] == sorted[1] or
        sorted[1] == sorted[2] or
        sorted[2] == sorted[3] or
        sorted[3] == sorted[4]):
        return True
    else:
        return False

def highCard(cards):
    sorted = []
    for i in range(len(cards)):
        sorted.append(hand[i])
    sorted.sort()

# returns hand with lowest value by card values
def compareHands(hand1, hand2):
    cardSort = "23456789TJQKA"
    for i in range(len(hand1)):
        if(cardSort.find(hand1[i]) < cardSort.find(hand2[i])):
            return hand1
        elif(cardSort.find(hand2[i]) < cardSort.find(hand1[i])):
            return hand2

# hands - cards, bid, type (1-7)
hands = []
for i in range(len(data)):
    hands.append([data[i][0:5], int(data[i][6:]), 0])

# figure out what hand they got dealt
for i in range(len(hands)):
    hand = hands[i][0]
    if fiveKind(hand) :
        hands[i][2] = 7
    elif fourKind(hand):
        hands[i][2] = 6
    elif fullHouse(hand):
        hands[i][2] = 5
    elif threeKind(hand):
        hands[i][2] = 4
    elif twoPair(hand):
        hands[i][2] = 3
    elif onePair(hand):
        hands[i][2] = 2
    else:
        hands[i][2] = 1


# sort list by rankings
rankings = []
# sort into new list that is ordered by ranking 1-7 then card value
# use the compareHands(hand1, hand2) function to compare them and sort
# shouldn't make a new list - should use pop() instead and keep in hands list
for i in range(1, len(hands)):
    done = False
    for j in range(0, i):
        # find the correct rank
        if(hands[i][2] < hands[j][2]):
            hands.insert(j, hands.pop(i))
            done = True
            break
        elif(hands[i][2] == hands[j][2]):
            if(compareHands(hands[i][0], hands[j][0]) == hands[i][0]):
                hands.insert(j, hands.pop(i))
                done = True
                break

print(hands)
total = 0
for i in range(len(hands)):
    print(hands[i])
    total += hands[i][1] * (i + 1)
print(total)



