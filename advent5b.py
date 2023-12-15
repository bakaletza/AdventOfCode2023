# Amy Bakaletz - 2023

# This code works on test data but crashes on real data due to lists too long - will fix later, maybe

# l1 = list
# m = mapping
# returns l2
def processMap(l1, m):
    # now process each seed
    l2 = []
    for i in range(len(l1)):
        value = l1[i]
        for j in range(len(m)):
            dest = m[j][0]
            source = m[j][1]
            ran = m[j][2]
            if (l1[i] > source and l1[i] < source + ran):
                if(source < dest):
                    value = value + abs(source - dest)
                else:
                    value = value - abs(source - dest)
                break
            elif(l1[i] == source):
                value = dest
                break
        l2.append(value)
        #print(str(l1[i]) + " - " + str(l2[i]))
    return l2

def makeMap(d):
    global row
    m = []
    while row < len(data) and data[row] != "":
        nums = [int(x) for x in data[row].split()]
        m.append([nums[0], nums[1], nums[2]])
        row += 1
    return m

# read in the data file
file = open("advent5test.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

# load all the lists
# seed ranges to be processed
print("processing seeds")
seeds = []
seedRanges = [int(x) for x in data[0][7:].split()]
for i in range(0, len(seedRanges), 2):
    for j in range(seedRanges[i + 1]):
        seeds.append(seedRanges[i] + j)
print("seeds ", end = "")
print(seeds)

# seeds to soil
print("processing soil")
row = 3
mapping = makeMap(data)
soil = processMap(seeds, mapping)
print("soil ", end = "")
print(soil)

# soil to fertilizer
print("processing fert")
row += 2
mapping = makeMap(data)
fert = processMap(soil, mapping)
print("fert ", end = "")
print(fert)

# fertilizer to water
print("processing water")
row += 2
mapping = makeMap(data)
water = processMap(fert, mapping)
print("water ", end = "")
print(water)

# water to light
print("processing light")
row += 2
mapping = makeMap(data)
light = processMap(water, mapping)
print("light ", end = "")
print(light)

# light to temp
print("processing temp")
row += 2
mapping = makeMap(data)
temp = processMap(light, mapping)
print("temp ", end = "")
print(temp)

# temp to humidity
print("processing humidity")
row += 2
mapping = makeMap(data)
humidity = processMap(temp, mapping)
print("humi ", end = "")
print(humidity)

# humidity to location
print("processing location")
row += 2
mapping = makeMap(data)
location = processMap(humidity, mapping)
print("location ", end = "")
print(location)

print(min(location))


