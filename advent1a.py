# read in the data file

file = open("advent1test.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

calibration = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if((data[i][j]).isdigit()):
            first = int(data[i][j])
            last = first
            break
    for j in range(len(data[i])-1,0,-1):
         if((data[i][j]).isdigit()):
            last = int(data[i][j])
            break
    calibration += int(first) * 10 + int(last)
print(calibration)
