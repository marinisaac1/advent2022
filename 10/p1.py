addxTime = 2
noopTime = 1
cyclesMatter = [20 + x * 40 for x in range(6)]

def cycleCalculator(operations: list) -> int:
    cycleNumber = 0
    x = 1
    totalSignal = 0
    for op in operations:
        command = op[:4]
        if command == 'addx':
            commandTime = 2
            value = int(op[5:])
        elif command == 'noop':
            commandTime = 1
        for t in range(commandTime):
            cycleNumber += 1
            if cycleNumber in cyclesMatter:
                totalSignal += x * cycleNumber
        if command == 'addx':
            x += int(value)
    return totalSignal

with open('input.txt', 'r') as f:
    text = f.read().splitlines()
print(cycleCalculator(text))