file = open("advent6.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

time = int(data[0][10:].replace(" ",""))
dist = int(data[1][10:].replace(" ",""))

winner = 0

for button in range(1, time-1):
    distance = (time - button) * button
    if(distance > dist):
        winner += 1

print(winner)
