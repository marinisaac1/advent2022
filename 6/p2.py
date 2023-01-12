with open('input.txt', 'r') as f:
    text = f.read()
for i in range(14, len(text)):
    letters = set()
    for j in range(i-14, i):
        if text[j] in letters:
            break
        else:
            letters.add(text[j])
    if len(letters) == 14:
        print(i)
        break