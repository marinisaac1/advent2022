# Read a text file
with open('input.txt', 'r') as f:
    text = f.read()

lines = text.split('\n')
maxCal = 0
currentCal = 0
pos = -1
i=0

for line in lines:
    if line == '':
        if currentCal > maxCal:
            print(maxCal)
            maxCal = currentCal
            pos = i
        currentCal = 0
        i += 1
    else:
        currentCal = currentCal + int(line)

print(f'Position: {pos} has the maximum calories: {maxCal}')