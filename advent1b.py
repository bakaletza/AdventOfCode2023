# read in the data file

file = open("advent1.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

calibration = 0
for i in range(len(data)):
    # FIND FIRST NUMBER

    # make list of positions, position 0 is the digit rest are the number
    positions = []
    foundDigit = False
    # find the position of the first acutal digit (-1 if there isn't one)
    for j in range(len(data[i])):
        if((data[i][j]).isdigit()):
            positions.append(j)
            firstdigit = int(data[i][j])
            foundDigit = True
            break
    if(not foundDigit):
        positions.append(-1)
    # fill rest of array with position of each of the words
    positions.append(data[i].find("one"))
    positions.append(data[i].find("two"))
    positions.append(data[i].find("three"))
    positions.append(data[i].find("four"))
    positions.append(data[i].find("five"))
    positions.append(data[i].find("six"))
    positions.append(data[i].find("seven"))
    positions.append(data[i].find("eight"))
    positions.append(data[i].find("nine"))

    # now see which number came first using by finding smallest positive #
    pos = 10
    for j in range(len(positions)):
        #print(str(positions[j]) + " < " + str(positions[pos]))
        if(positions[j] >= 0):
            if(pos == 10):
                pos = j
            elif(positions[j] < positions[pos]):
                pos = j
    if pos == 0:
        first = firstdigit
    else:
        first = pos
    #last = first # in case only one number

    #FIND LAST NUMBER

    # find the position of the last actual digit (-1 if there isn't one)
    foundDigit = False
    for j in range(len(data[i])-1, -1, -1):
        if((data[i][j]).isdigit()):
            positions[0] = j
            lastdigit = int(data[i][j])
            foundDigit = True
            break
    if(not foundDigit):
        positions[0] = -1

    #update positions to be last occurrence
    positions[1] = data[i].rfind("one")
    positions[2] = data[i].rfind("two")
    positions[3] = data[i].rfind("three")
    positions[4] = data[i].rfind("four")
    positions[5] = data[i].rfind("five")
    positions[6] = data[i].rfind("six")
    positions[7] = data[i].rfind("seven")
    positions[8] = data[i].rfind("eight")
    positions[9] = data[i].rfind("nine")

    # find last index of either a digit or a word number
    pos = 10
    for j in range(len(positions)-1, -1, -1):
        # print(str(positions[j]) + " < " + str(positions[pos]))
        if (positions[j] >= 0):
            if (pos == 10):
                pos = j
            elif (positions[j] > positions[pos]):
                pos = j
    if pos == 0:
        last = lastdigit
    else:
        last = pos
    # check and see if the last char in string is actually a digit
    if data[i][-1].isdigit():
        last = int(data[i][-1])

    # add to calibration total
    calibration += first * 10 + last
print(calibration)
