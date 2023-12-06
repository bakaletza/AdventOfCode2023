file = open("advent6.txt", "r")
data = file.read().strip('\n\r').splitlines()
file.close()

time = [int(x) for x in data[0][10:].split()]
dist = [int(x) for x in data[1][10:].split()]
print(time)
print(dist)

total = 1
for i in range(len(time)):
    winner = 0
    for button in range(1, time[i]-1):
        distance = (time[i] - button) * button
        if(distance > dist[i]):
            winner += 1
    print(winner)
    if(winner > 0):
        total *= winner
print(total)
