# read in the data file

file = open("advent1.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

print(data)
