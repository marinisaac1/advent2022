def simulateCrate(stacks: list, stackFrom: int, stackTo: int, amountContainers: int) -> list:
    for i in range(amountContainers):
        stacks[stackTo].insert(0,(stacks[stackFrom].pop(0)))

def parser(text: str) -> set:
    stacks = {}
    movements = []
    startMovements = 0
    for i, line in enumerate(text.split('\n')):
        stackPos = 0
        stackPos = line.find('[', stackPos)
        while stackPos != -1:
            stackIndex = (stackPos // 4) + 1
            stacks.setdefault(stackIndex, []).append(line[stackPos + 1])
            stackPos = line.find('[', stackPos + 1)
            if stackPos == -1:
                startMovements = i + 3
    for line in text.split('\n')[startMovements:]:
        movement = {}
        startAmount = 5
        startFrom = int(line.find(' from ')) + 6
        startTo = int(line.find(' to ')) + 4
        movement['amount'] = int(line[startAmount: startFrom - 6])
        movement['from'] = int(line[startFrom: startTo - 4])
        movement['to'] = int(line[startTo:])
        movements.append(movement)
    return stacks, movements

with open('input.txt', 'r') as f:
    text = f.read()
    stacks, movements = parser(text)
    print(stacks)
    for movement in movements:
        print(movement)
        simulateCrate(stacks, movement['from'], movement['to'], movement['amount'])
        print(stacks)

topStacks = ''
for i in range(1, len(stacks) + 1):
    topStacks += stacks[i][0]
print(topStacks)