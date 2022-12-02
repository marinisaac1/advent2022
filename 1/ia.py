import re

def find_elf_with_most_calories(input_string: str) -> int:
    # Split the input string into a list of strings, using a regular expression
    # that matches any sequence of two or more newline characters
    lines = re.split(r'\n{2,}', input_string)

    # Split the list of strings into a list of lists of strings, with one
    # sublist per Elf, and remove any empty strings from the list
    elves = [list(filter(None, x.split())) for x in lines]

    # Convert the list of lists of strings to a list of lists of integers, and
    # remove any empty lists from the list
    elves = [list(map(int, x)) for x in elves if x]

    # Find the total number of Calories carried by each Elf, and return the
    # maximum value
    return max([sum(x) for x in elves])


input_string = '''
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''
with open('input.txt', 'r') as f:
    text = f.read()
print(find_elf_with_most_calories(text))