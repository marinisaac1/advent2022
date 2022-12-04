def findSharedItems(left: str, right: str) -> list:
    common = []
    for letter in left:
        if letter in right:
            common.append(letter)
    return common

totalPriority = 0

with open('input.txt', 'r') as f:
    text = f.read()
    for line in text.split('\n'):
        left = set(line[:len(line) // 2])
        right = set(line[len(line) // 2:])
        common = findSharedItems(left, right)
        for letter in common:
            if letter.isupper():
                totalPriority += ord(letter) - ord('A') + 27
            else:
                totalPriority += ord(letter) - ord('a') + 1
        

print(totalPriority)