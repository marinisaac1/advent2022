import time
import copy

def findStart(map: list) -> tuple:
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 'S':
                return x, y

def printMap(map: list):
    for line in map:
        print(''.join(line))

def explore(visitedMap: list, currentX, currentY, currentHeight) -> list:
    #print('*'*20)
    #print('Current X: ', currentX, 'Current Y: ', currentY)
    #printMap(visitedMap)
    #time.sleep(0.1)

    # Create the own copy of the map
    map = copy.deepcopy(visitedMap)

    # Get ascii from current letter
    currentLetter = map[currentY][currentX]
    if currentHeight == ord('z') and currentLetter == 'E':
        return [map]

    currentHeight = ord(currentLetter)

    answers = []

    # Check if up is non visited already
    if currentY != 0 and map[currentY - 1][currentX].isalpha():
        newLetter = map[currentY - 1][currentX]
        # Get ascii from new letter
        newHeight = ord(newLetter)
        # Check if new is reachable
        if newHeight - currentHeight <= 1:
            # print('up')
            map[currentY][currentX] = '^'
            up = explore(map, currentX, currentY - 1, currentHeight)
            for m in up:
                answers.append(m)

    # Check if down is non visited already
    if currentY != len(map) - 1 and map[currentY + 1][currentX].isalpha():
        newLetter = map[currentY + 1][currentX]
        # Get ascii from new letter
        newHeight = ord(newLetter)
        # Check if new is reachable
        if newHeight - currentHeight <= 1:
            # print('down')
            map[currentY][currentX] = '*'
            down = explore(map, currentX, currentY + 1, currentHeight)
            for m in down:
                answers.append(m)
    
    # Check if left is non visited already
    if currentX != 0 and map[currentY][currentX - 1].isalpha():
        newLetter = map[currentY][currentX - 1]
        # Get ascii from new letter
        newHeight = ord(newLetter)
        # Check if new is reachable
        if newHeight - currentHeight <= 1:
            # print('left')
            map[currentY][currentX] = '<'
            left = explore(map, currentX - 1, currentY, currentHeight)
            for m in left:
                answers.append(m)
    
    # if currentX == 0 and currentY == 1:
    #     print('Aqui debe dar vuelta')
    #     printMap(map)

    # Check if right is non visited already
    if currentX != len(map[0]) - 1 and map[currentY][currentX + 1].isalpha():
        newLetter = map[currentY][currentX + 1]
        # Get ascii from new letter
        newHeight = ord(newLetter)
        # Check if new is reachable
        if newHeight - currentHeight <= 1:
            # print('right')
            map[currentY][currentX] = '>'
            right = explore(map, currentX + 1, currentY, currentHeight)
            for m in right:
                answers.append(m)
    
    return answers

with open('input.txt', 'r') as f:
    map = f.read().splitlines()
    map = [list(line) for line in map]
    start = findStart(map)

    map[start[1]][start[0]] = 'a'

    answers = explore(map, start[0], start[1], ord('a'))
    #print(answers)
    steps = []
    for answer in answers:
        stepsInAnswer = 0
        for i in range(len(answer)):
            for j in range(len(answer[i])):
                if answer[i][j] in ['^', '*', '<', '>']:
                    stepsInAnswer += 1
        steps.append(stepsInAnswer)
        if stepsInAnswer == 25:
            print('Answer: ')
            printMap(answer)
    steps.sort()
    print(steps)
    minSteps = steps[0]
print(minSteps)