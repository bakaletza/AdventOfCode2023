# functions
def equalColumns(l, col1, col2):
    same = True
    for row in range(len(l)):
        if(l[row][col1] != l[row][col2]):
            same = False
    return same

def findHorizontal(n):
    global hRow
    found = False
    for j in range(len(n) - 1):
        if(n[j] == n[j + 1] and j+1 != hRow):
            found = True
            above = j - 1
            below = j + 2
            while (found and above >= 0 and below < len(n)):
                if(n[above] != n[below]):
                    found = False
                    break
                above -= 1
                below += 1
            if(found):
                return (j + 1)
    return -1

def findVertical(n):
    global vCol
    for j in range(len(n[0]) - 1):
        if (equalColumns(n, j, j + 1) and j+1 != vCol):
            found = True
            left = j - 1
            right = j + 2
            while (found and left >= 0 and right < len(n[0])):
                if (not equalColumns(n, left, right)):
                    found = False
                    break
                left -= 1
                right += 1
            if (found):
                return j + 1
    return -1

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
        notes.append(list(data[i]))
        i += 1
    i += 1
    # process each note
    hRow = -1
    vCol = -1
    # first check for horizontal
    hRow = findHorizontal(notes)
    if hRow >= 0:
        print("horizontal reflection in note " + str(note) + " at row " + str(hRow))
    else:
        # check for vertical
        vCol = findVertical(notes)
        if (vCol >= 0):
            print("vertical reflection in note " + str(note) + " at col " + str(vCol))

    # now find the smudge, looking for a  different hRow or vCol
    for r in range(len(notes)):
        found = False
        for c in range(len(notes[0])):
            # change
            if notes[r][c] == ".":
                notes[r][c] = "#"
            else:
                notes[r][c] = "."

            # check if horizontal or vertical mirror
            newRow = findHorizontal(notes)
            if newRow >= 0 and newRow != hRow:
                print("SMUDGE horizontal reflection in note " + str(note) + " at row " + str(newRow))
                sum += (newRow) * 100
                found = True
                break
            else:
                # check for vertical
                newCol = findVertical(notes)
                if (newCol >= 0 and newCol != vCol):
                    print("SMUDGE vertical reflection in note " + str(note) + " at col " + str(newCol))
                    sum += newCol
                    found = True
                    break

           # not found - change back
            if notes[r][c] == ".":
                notes[r][c] = "#"
            else:
                notes[r][c] = "."
        if found:
            break

print(sum)
