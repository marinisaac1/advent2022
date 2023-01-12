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
        for j in range(0, x, 1):
            # Edges
            numberPos = int(text[i][j])
            if i == 0 or j == 0 or i == y - 1 or j == x - 1:
                right[i][j] = 1
                max = numberPos
            if numberPos > max:
                right[i][j] = 1
                max = numberPos
    # Check left
    for i in range(0, y, 1):
        max = 0
        for j in range(x-1, -1, -1):
            # Edges
            numberPos = int(text[i][j])
            if i == 0 or j == 0 or i == y - 1 or j == x - 1:
                left[i][j] = 1
                max = numberPos
            if numberPos > max:
                left[i][j] = 1
                max = numberPos
    # Check down
    for i in range(0, x, 1):
        max = 0
        for j in range(0, y, 1):
            # Edges
            numberPos = int(text[j][i])
            if i == 0 or j == 0 or i == y - 1 or j == x - 1:
                down[j][i] = 1
                max = numberPos
            if numberPos > max:
                down[j][i] = 1
                max = numberPos
    # Check up
    for i in range(0, x, 1):
        max = 0
        for j in range(y-1, -1, -1):
            # Edges
            numberPos = int(text[j][i])
            if i == 0 or j == 0 or i == y - 1 or j == x - 1:
                up[j][i] = 1
                max = numberPos
            if numberPos > max:
                up[j][i] = 1
                max = numberPos
    totalVisible = 0
    for i in range(0, y, 1):
        for j in range(0, x, 1):
            if right[i][j] == 1 or left[i][j] == 1 or up[i][j] == 1 or down[i][j] == 1:
                totalVisible += 1
    return totalVisible

with open('input.txt', 'r') as f:
    text = f.readlines()
print(countVisible(text))