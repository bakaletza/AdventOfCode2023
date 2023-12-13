# functions
def equalColumns(l, col1, col2):
    same = True
    for row in range(len(l)):
        if(l[row][col1] != l[row][col2]):
            same = False
    return same

# read in the data file
file = open("advent13.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

i = 0
note = 0
sum = 0
while i < len(data):
    note += 1
    notes = []
    while(i < len(data) and data[i] != ""):
        notes.append(data[i])
        i += 1
    i += 1
    # process notes
    # first check for horizontal
    found = False
    for j in range(len(notes) - 1):
        if(notes[j] == notes[j + 1]):
            found = True
            above = j - 1
            below = j + 2
            while (found and above >= 0 and below < len(notes)):
                if(notes[above] != notes[below]):
                    found = False
                    break
                above -= 1
                below += 1

            if(found):
                print("horizontal reflection in note " + str(note) + " at row " + str(j + 1))
                sum += (j + 1) * 100
                print(sum)

    if not found:
        # check for vertical
        for j in range(len(notes[0]) - 1):
            if (equalColumns(notes, j, j + 1)):
                found = True
                left = j - 1
                right = j + 2
                while (found and left >= 0 and right < len(notes[0])):
                    if (not equalColumns(notes, left, right)):
                        found = False
                        break
                    left -= 1
                    right += 1

                if (found):
                    print("vertical reflection in note " + str(note) + " at col " + str(j + 1))
                    sum += (j + 1)
                    print(sum)

print(sum)
