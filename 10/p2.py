addxTime = 2
noopTime = 1
cyclesMatter = [x * 40 for x in range(6)]



def cycleCalculator(operations: list) -> str:
    output = ""
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
            if cycleNumber % 40 in [x-1, x, x+1]:
                output += "#"
            else:
                output += "."
            cycleNumber += 1
            if cycleNumber in cyclesMatter:
                output += "\n"
        if command == 'addx':
            x += int(value)
    return output

with open('input.txt', 'r') as f:
    text = f.read().splitlines()
print(cycleCalculator(text))