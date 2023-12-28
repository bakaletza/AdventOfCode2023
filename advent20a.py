file = open("advent20.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

# create all the objects
class FlipFlop:
    def __init__(self, name, status, dest):
        self.name = name
        self.status = status
        self.dest = dest
    def __str__(self):
        return f"% {self.name} {self.status} - {self.dest}"

class ConInput:
    def __init__(self, name, pulse):
        self.name = name
        self.pulse = pulse

    def __str__(self):
        return f" {self.name}  {self.pulse}"

class Conjunction:
    def __init__(self, name, inputs, dest):
        self.name = name
        self.inputs = inputs # name, high/low
        self.dest = dest
    def __str__(self):
        return f"& {self.name} {self.status} - {self.dest}"
class UnTyped:
    def __init__(self, name):
        self.name = name
        self.dest = []
    def __str__(self):
        return f"  {self.name}"

modules = []
# add typed modules and broadcaster
for i in range(len(data)):
    space = data[i].find(" ")
    secondSpace = data[i].find(" ", space + 1)
    type = data[i][0]
    if(type == "b"):
        secondSpace = data[i].find(" ",space+1)
        broadcaster = data[i][secondSpace+1:].split(", ")
    else:
        name = data[i][1:space]
        dest = data[i][secondSpace+1:].split(", ")
        if type == "%":
            modules.append(FlipFlop(name,"off",dest))
        else:
            modules.append(Conjunction(name,[],dest))

# check for untyped modules
for i in range(len(modules)):
    for j in range(len(modules[i].dest)):
        found = False
        for k in range(len(modules)):
            if(modules[i].dest[j] == modules[k].name):
                found = True
        if not found:
            modules.append(UnTyped(modules[i].dest[j]))

# set up all the inputs for the conjunction modules
for i in range(len(modules)):
    if isinstance(modules[i], Conjunction):
        for j in range(len(modules)):
            for k in range(len(modules[j].dest)):
                if modules[j].dest[k] == modules[i].name:
                    modules[i].inputs.append(ConInput(modules[j].name, "low"))

# push the button 1000 times
low = 0
high = 0
queue = []
for i in range(1000):
    low += 1 # low pulse sent from button to broadcaster
    for j in range(len(broadcaster)):
        # send low pulse from broadcaster to each module
        queue.append(["broadcaster", "low", broadcaster[j]])
    while len(queue) != 0:
        next = queue.pop(0) # from, pulse, to
        if(next[1] == "low"):
            low += 1
        else:
            high += 1
        print(next)
        # find the item in the list of modules
        for j in range(len(modules)):
            if(next[2] == modules[j].name):
                break
        # process
        if isinstance(modules[j], FlipFlop):
            if(next[1] == "low"):
                if modules[j].status == "off":
                    modules[j].status = "on"
                    for k in range(len(modules[j].dest)):
                        queue.append([modules[j].name, "high", modules[j].dest[k]])
                else:
                    modules[j].status = "off"
                    for k in range(len(modules[j].dest)):
                        queue.append([modules[j].name, "low", modules[j].dest[k]])
        elif isinstance(modules[j], Conjunction):
            # update status for this input - if first time it will be "low", otherwise it will be next[0
            for k in range(len(modules[j].inputs)):
                if(modules[j].inputs[k].name == next[0]):
                    break
            modules[j].inputs[k].pulse = next[1]

            # if high pulses for all inputs, send a low pulse
            # else send a high pulse
            allHigh = True
            for k in range(len(modules[j].inputs)):
                if modules[j].inputs[k].pulse == "low":
                    allHigh = False
                    break
            # send signals to destinations
            for k in range(len(modules[j].dest)):
                if allHigh:
                    queue.append([modules[j].name, "low", modules[j].dest[k]])
                else:
                    queue.append([modules[j].name, "high", modules[j].dest[k]])

print("low " + str(low))
print("high " + str(high))
print("total pulses " + str(low * high))



