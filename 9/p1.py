def simulateKnot(text: list) -> int:
    hX = 0
    hY = 0
    tX = 0
    tY = 0
    visitedCells = set()
    for i in range(0, len(text)):
        direction, moves = text[i].split()
        print(f"direction: {direction}, moves: {moves}")
        for n in range(int(moves)):
            if direction == 'R':
                hX += 1
            elif direction == 'L':
                hX -= 1
            elif direction == 'U':
                hY += 1
            elif direction == 'D':
                hY -= 1
            tX, tY = followHead(hX, hY, tX, tY)
            visitedCells.add(f"{tX}, {tY}")
        print(f"hX: {hX}, hY: {hY}, tX: {tX}, tY: {tY}")
    return len(visitedCells)

def followHead(hX: int, hY: int, tX: int, tY: int) -> set:
    # Check if head is in tail
    if hX == tX and hY == tY:
        return tX, tY
    # Check if head is in same row as tail
    elif hY == tY:
        if abs(hX - tX) > 1:
            if hX > tX:
                tX += 1
            elif hX < tX:
                tX -= 1
    # Check if head is in same column as tail
    elif hX == tX:
        if abs(hY - tY) > 1:
            if hY > tY:
                tY += 1
            elif hY < tY:
                tY -= 1
    # Check if head is in a different row and column than tail
    else:
        if abs(hX - tX) > 1 or abs(hY - tY) > 1:
            if hX > tX and hY > tY:
                tX += 1
                tY += 1
            elif hX < tX and hY < tY:
                tX -= 1
                tY -= 1
            elif hX > tX and hY < tY:
                tX += 1
                tY -= 1
            elif hX < tX and hY > tY:
                tX -= 1
                tY += 1
    return tX, tY


with open('input.txt', 'r') as f:
    text = f.read().splitlines()
print(simulateKnot(text))