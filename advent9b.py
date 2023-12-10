# read in the data file
file = open("advent9.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

sum = 0
for i in range(len(data)):
    nums = []
    nums.append([int(x) for x in data[i].split()])
    allZeros = False
    row = 0
    while not allZeros:
        allZeros = True
        nums.append([])
        row += 1
        for j in range(1, len(nums[row-1])):
            diff = nums[row-1][j] - nums[row-1][j-1]
            nums[row].append(diff)
            if(diff != 0):
                allZeros = False
    # extrapolate
    nums[row].insert(0,0)
    row -= 1
    while row >= 0:
        value = nums[row][0] - nums[row+1][0]
        nums[row].insert(0,value)
        if row == 0:
            sum += value
        row -= 1

    print(nums)
print(sum)
