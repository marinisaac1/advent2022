def findFullyContained(first: str, second: str) -> bool:
    first = first.split('-')
    second = second.split('-')
    beginFirst = int(first[0])
    endFirst = int(first[1])
    beginSecond = int(second[0])
    endSecond = int(second[1])
    if beginFirst <= beginSecond and endFirst >= endSecond or beginFirst >= beginSecond and endFirst <= endSecond:
        return True

totalFullyContained = 0

with open('input.txt', 'r') as f:
    text = f.read()
    lines = text.split('\n')
    for line in lines:
        line = line.split(',')
        if findFullyContained(line[0], line[1]):
            totalFullyContained += 1

print(totalFullyContained)