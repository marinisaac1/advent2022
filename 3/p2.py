def findSharedItems(first: set, second: set, third: set) -> str:
    for letter in first:
        if letter in second and letter in third:
            return letter

totalPriority = 0

with open('input.txt', 'r') as f:
    text = f.read()
    lines = text.split('\n')
for i in range(0, len(lines), 3):
    first = set(lines[i])
    second = set(lines[i + 1])
    third = set(lines[i + 2])
    common = findSharedItems(first, second, third)
    if common.isupper():
        totalPriority += ord(common) - ord('A') + 27
    else:
        totalPriority += ord(common) - ord('a') + 1
        

print(totalPriority)