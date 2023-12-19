# read in the data file
file = open("advent12test.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

# load up the lists
springs = []
damaged = []
for i in range(len(data)):
    space = data[i].find(" ")
    springs.append(data[i][0:space])
    damaged.append(data[i][space+1:].split(","))
    damaged[i] = [int(x) for x in damaged[i]]

# find the number of arrangements for each element
sum = 0
for i in range(len(damaged)):
    arrangements = 0

    sum += arrangements

print(sum)
