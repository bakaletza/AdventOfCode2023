file = open("advent19.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

# load workflow
workflow = []
i = 0
while data[i] != "":
    workflow.append([])
    bracket = data[i].find("{")
    workflow[i].append(data[i][0:bracket])
    flow = data[i][bracket+1:-1].split(",")
    for j in range(len (flow)):
        workflow[i].append(flow[j])
    i += 1
i += 1

#load parts
parts = []
# x,m,a,s
k = 0
for j in range(i, len(data)):
    parts.append([])
    firstComma = data[j].find(",")
    parts[k].append(int(data[j][3:firstComma]))
    secondComma = data[j].find(",", firstComma+1)
    parts[k].append(int(data[j][firstComma+3:secondComma]))
    thirdComma = data[j].find(",", secondComma+1)
    parts[k].append(int(data[j][secondComma+3:thirdComma]))
    parts[k].append(int(data[j][thirdComma+3:-1]))
    k+=1

# find location of the "in" workflow so you don't have to repeat this:
for start in range(len(workflow)):
    if (workflow[start][0] == "in"):
        break

sum = 0
for i in range(len(parts)):
    # set up the starting values
    wf = start
    wfPos = 1
    cat = workflow[wf][wfPos][0:1]
    operator = workflow[wf][wfPos][1:2]
    colon = workflow[wf][wfPos].find(":")
    value = int(workflow[wf][wfPos][2:colon])
    dest = workflow[wf][wfPos][colon + 1:]
    comma = workflow[wf][wfPos].find(",")
    done = False
    while not done:
        # do the comparison
        if cat == "x":
            index = 0
        elif cat == "m":
            index = 1
        elif cat == "a":
            index = 2
        else:
            index = 3
        if (operator == "<" and parts[i][index] < value) or (operator == ">" and parts[i][index] > value):
            # true - move on to the next workflow or quit if A/R
            if dest == "A" or dest == "R":
                done = True
            else:
                for wf in range(len(workflow)):
                    if (workflow[wf][0] == dest):
                        break
                wfPos = 1
                cat = workflow[wf][wfPos][0:1]
                operator = workflow[wf][wfPos][1:2]
                colon = workflow[wf][wfPos].find(":")
                value = int(workflow[wf][wfPos][2:colon])
                dest = workflow[wf][wfPos][colon + 1:]
        else:
            # false - move on to the next item and determine dest
            wfPos += 1
            colon = workflow[wf][wfPos].find(":")
            if(colon == -1):
                # final item in this WF
                dest = workflow[wf][wfPos]
                if(dest == "A" or dest == "R"):
                    done = True
                else:
                    for wf in range(len(workflow)):
                        if (workflow[wf][0] == dest):
                            break
                    wfPos = 1
                    cat = workflow[wf][wfPos][0:1]
                    operator = workflow[wf][wfPos][1:2]
                    colon = workflow[wf][wfPos].find(":")
                    value = int(workflow[wf][wfPos][2:colon])
                    dest = workflow[wf][wfPos][colon + 1:]
            else:
                # set up for next comparison
                cat = workflow[wf][wfPos][0:1]
                operator = workflow[wf][wfPos][1:2]
                colon = workflow[wf][wfPos].find(":")
                value = int(workflow[wf][wfPos][2:colon])
                dest = workflow[wf][wfPos][colon + 1:]

    # finished this part - if accepted add to total
    if(dest == "A"):
        sum += (parts[i][0] + parts[i][1] + parts[i][2] + parts[i][3])

print(sum)







