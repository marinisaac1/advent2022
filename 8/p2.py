def countVisible(text: list) -> int:
    x = len(text[0])-1
    y = len(text)
    # visible matrices
    # 0 = not visible
    # 1 = visible
    right = [[0 for i in range(x)] for j in range(y)]
    left = [[0 for i in range(x)] for j in range(y)]
    up = [[0 for i in range(x)] for j in range(y)]
    down = [[0 for i in range(x)] for j in range(y)]
    # Check right
    for i in range(0, y, 1):
        max = 0
        previous = []
        for j in range(0, x, 1):
            # Edges
            visible = 0
            numberPos = int(text[i][j])
            for k in range(len(previous) - 1, -1, -1):
                if previous[k] >= numberPos:
                    visible += 1
                    break
                visible += 1
            right[i][j] = visible
            previous.append(numberPos)
    # Check left
    for i in range(0, y, 1):
        max = 0
        previous = []
        for j in range(x-1, -1, -1):
            visible = 0
            numberPos = int(text[i][j])
            for k in range(len(previous) - 1, -1, -1):
                if previous[k] >= numberPos:
                    visible += 1
                    break
                visible += 1
            left[i][j] = visible
            previous.append(numberPos)
    # Check down
    for i in range(0, x, 1):
        max = 0
        previous = []
        for j in range(0, y, 1):
            visible = 0
            numberPos = int(text[j][i])
            for k in range(len(previous) - 1, -1, -1):
                if previous[k] >= numberPos:
                    visible += 1
                    break
                visible += 1
            down[j][i] = visible
            previous.append(numberPos)
    # Check up
    for i in range(0, x, 1):
        max = 0
        previous = []
        for j in range(y-1, -1, -1):
            visible = 0
            numberPos = int(text[j][i])
            for k in range(len(previous) - 1, -1, -1):
                if previous[k] >= numberPos:
                    visible += 1
                    break
                visible += 1
            up[j][i] = visible
            previous.append(numberPos)
            
    maxVisible = 0
    for i in range(0, y, 1):
        for j in range(0, x, 1):
            totalVisible = right[i][j] * left[i][j] * up[i][j] * down[i][j]
            if totalVisible > maxVisible:
                maxVisible = totalVisible
    return maxVisible

with open('input.txt', 'r') as f:
    text = f.readlines()
print(countVisible(text))