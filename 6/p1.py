with open('input.txt', 'r') as f:
    text = f.read()
for i in range(4, len(text)):
    letters = set()
    for j in range(i-4, i):
        if text[j] in letters:
            break
        else:
            letters.add(text[j])
    if len(letters) == 4:
        print(i)
        break