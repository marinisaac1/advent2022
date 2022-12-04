def anyIntersection(first: str, second: str) -> bool:
    first = first.split('-')
    second = second.split('-')
    beginFirst = int(first[0])
    endFirst = int(first[1])
    beginSecond = int(second[0])
    endSecond = int(second[1])
    if beginFirst <= beginSecond and endFirst >= beginSecond or beginFirst <= endSecond and endFirst >= endSecond or beginSecond <= endFirst and endSecond >= endFirst or beginSecond <= beginFirst and endSecond >= beginFirst:
        return True

totalIntersect = 0

with open('input.txt', 'r') as f:
    text = f.read()
    lines = text.split('\n')
    for line in lines:
        line = line.split(',')
        if anyIntersection(line[0], line[1]):
            totalIntersect += 1

    print(totalIntersect)