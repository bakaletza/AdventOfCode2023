# Amy Bakaletz - 2023

# read in the data file
file = open("advent5test.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

# load all the lists
# seeds to be processed
seeds = [int(x) for x in data[0][7:].split()]
print(seeds)

# seeds to soil
seedsToSoil = []
row = 3

# START HERE loop through this 7 times to create a mapping table....

while data[row] != "":
    print(data[row])
    nums = [int(x) for x in data[row].split()]
    source = nums[1]
    dest = nums[0]
    r = nums[2]
    for i in range(r):
        seedsToSoil.append([source+i, dest+i])
    row += 1
for i in range(len(seedsToSoil)):
    print(seedsToSoil[i])

# now process each seed
for i in range(len(seeds)):
    found = False
    for j in range(len(seedsToSoil)):
        if(seedsToSoil[j][0] == seeds[i]):
            print("source " + str(seedsToSoil[j][0]) + " dest " + str(seedsToSoil[j][1]))
            found = True
    if(not found):
        print("source " + str(seeds[i]) + " dest " + str(seeds[i]))




