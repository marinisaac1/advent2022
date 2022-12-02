intA = ord('A')
intX = ord('X')
diffXA = intX - intA

def calculateScore(input: str) -> int:
    lines = input.split('\n')
    score = 0
    for line in lines:
        values = line.split(' ')
        them = ord(values[0])
        me = ord(values[1])-diffXA
        if me == them + 1 or me == them - 2:
            # I win the round
            score += 6
        elif me == them:
            # Draw
            score += 3
        # Add according to the tool used
        score += me - intA + 1
    return score

with open('input.txt', 'r') as f:
    text = f.read()
    score = calculateScore(text)

print(score)