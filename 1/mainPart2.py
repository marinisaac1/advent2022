# Read a text file
with open('input.txt', 'r') as f:
    text = f.read()

lines = text.split('\n')
maxCal = 0
currentCal = 0
pos = -1
i=0

topCalories = []

for line in lines:
    if line == '':
        if currentCal > maxCal:
            print(maxCal)
            maxCal = currentCal
            pos = i
        topCalories.append(currentCal)
        currentCal = 0
        i += 1
    else:
        currentCal = currentCal + int(line)

topCalories.sort()
top3Added = sum(topCalories[-3:])
print(f'Top 3 added: {top3Added}')

print(f'Elve: {pos} has the maximum calories: {maxCal}')