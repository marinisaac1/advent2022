import tqdm

class Monkey:
    def __init__(self, id, operation, test, throwTrue, throwFalse, items):
        self.id = id
        self.operation = operation
        self.test = test
        self.throwTrue = throwTrue
        self.throwFalse = throwFalse
        self.items = items
        self.inspectedItems = 0

        self.modulo = 1
        for i in str(self.test):
            self.modulo *= int(i)
    
    def evaluate(self, old):
        new = eval(self.operation)
        #new = new // 3
        return new
    
    def decideToThrow(self, item):
        if item % self.test == 0:
            return self.throwTrue
        else:
            return self.throwFalse

    def __str__(self) -> str:
        return f'''Monkey: {self.id}
Operation: {self.operation},
Test: {self.test},
Throw True: {self.throwTrue},
Throw False: {self.throwFalse},
Items: {self.items}
Inspected items: {self.inspectedItems}
Modulo: {self.modulo}
        '''



def monkey_business(list: str) -> int:
    LINE_PER_MONKEY = 7
    TURNS = 10000
    monkeys = {}
    for i in range(len(list) // LINE_PER_MONKEY + 1):
        id = i
        # Create items
        items = []
        for j in list[i * LINE_PER_MONKEY + 1][18:].split(', '):
            items.append(int(j))
        # Create operation
        operation = list[i * LINE_PER_MONKEY + 2][19:]
        # Create test
        test = int(list[i * LINE_PER_MONKEY + 3][21:])
        # Create throwTrue
        throwTrue = int(list[i * LINE_PER_MONKEY + 4][29:])
        # Create throwFalse
        throwFalse = int(list[i * LINE_PER_MONKEY + 5][30:])
        # Create monkey
        monkey = Monkey(id, operation, test, throwTrue, throwFalse, items)
        monkeys[id] = monkey
    
    totalModulo = 1
    for key, m in monkeys.items():
        totalModulo *= m.test

    for n in tqdm.tqdm(range(TURNS)):
        for key, m in monkeys.items():
            for i in range(len(m.items)):
                m.inspectedItems += 1
                item = m.items.pop(0)
                new = m.evaluate(item)
                receiver = m.decideToThrow(new)
                new = new % (totalModulo)
                monkeys[receiver].items.append(new)
    
    totalInspectedItems = []
    for key, m in monkeys.items():
        totalInspectedItems.append(m.inspectedItems)
        print(m)
    totalInspectedItems.sort()
    return totalInspectedItems[-2] * totalInspectedItems[-1]

with open('input.txt', 'r') as f:
    text = f.read().splitlines()
print(monkey_business(text))