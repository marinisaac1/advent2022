def simulateKnot(text: list) -> int:
    totalKnots = 10
    X = [0 for i in range(totalKnots)]
    Y = [0 for i in range(totalKnots)]
    visitedCells = set()
    for i in range(0, len(text)):
        direction, moves = text[i].split()
        print(f"direction: {direction}, moves: {moves}")
        for n in range(int(moves)):
            if direction == 'R':
                X[0] += 1
            elif direction == 'L':
                X[0] -= 1
            elif direction == 'U':
                Y[0] += 1
            elif direction == 'D':
                Y[0] -= 1
            for k in range(1, totalKnots, 1):
                X[k], Y[k] = followHead(X[k-1], Y[k-1], X[k], Y[k])
            visitedCells.add(f"{X[9]}, {Y[9]}")
            
        for k in range(totalKnots):
            print(f"K: {k} X: {X[k]}, Y: {Y[k]}")
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