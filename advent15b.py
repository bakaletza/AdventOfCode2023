file = open("advent15.txt", "r")
data = file.read().strip('\n\r').split(",")
file.close()

def getHASH(str):
    cv = 0
    for j in range(len(str)):
        cv += ord(str[j])
        cv *= 17
        cv %= 256
    return cv

boxes = []
for i in range(256):
    boxes.append([])
for i in range(len(data)):
    findOp = data[i].find("=")
    if(findOp == -1):
        findOp = data[i].find("-")
    label = data[i][0:findOp]
    box = getHASH(label)
    operator = data[i][findOp]
    if(operator == "="):
        focal = data[i][findOp+1:]
        found = False
        for j in range(len(boxes[box])):
            space = boxes[box][j].find(" ")
            if(boxes[box][j][0:space] == label):
                # replace
                boxes[box][j] = label + " " + focal
                found = True
                break
        if not found:
            # add
            boxes[box].append(label + " " + focal)
    else:
        for j in range(len(boxes[box])):
            space = boxes[box][j].find(" ")
            if (boxes[box][j][0:space] == label):
                # remove
                boxes[box].pop(j)
                break

totalPower = 0
for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        box = i + 1
        slot = j + 1
        focal = int(boxes[i][j][-1])
        power = box * slot * focal
        print("box " + str(i) + " - " + boxes[i][j], end = " - ")
        print(str(box) + " * " + str(slot) + " * " + str(focal) + " = " + str(power))
        totalPower += power
print(totalPower)
