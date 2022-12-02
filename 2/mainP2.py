intA = ord('A')
intX = ord('X')
diffXA = intX - intA

wins = {'A': 'B', 'B': 'C', 'C': 'A'}
losses = {'A': 'C', 'B': 'A', 'C': 'B'}
win = 'Z'
draw = 'Y'
loss = 'X'

def calculateScore(input: str) -> int:
    lines = input.split('\n')
    score = 0
    for line in lines:
        values = line.split(' ')
        them = values[0]
        me = values[1]
        if me == win:
            score += 6
            score += ord(wins[them]) - intA + 1
        elif me == draw:
            score += 3
            score += ord(them) - intA + 1
        elif me == loss:
            score += 0 
            score += ord(losses[them]) - intA + 1

    return score

with open('input.txt', 'r') as f:
    text = f.read()
    score = calculateScore(text)

print(score)