file = open("advent15.txt", "r")
data = file.read().strip('\n\r').split(",")
file.close()

sum = 0
for i in range(len(data)):
    currentValue = 0
    for j in range(len(data[i])):
        currentValue += ord(data[i][j])
        currentValue *= 17
        currentValue %= 256
    print(data[i] + " " + str(currentValue))
    sum += currentValue
print(sum)
