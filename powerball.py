import random as rand

entries = []

numberOfEntries = 0

while (numberOfEntries <= 0):
    try:
        numberOfEntries = int(input("How many entries do you want?"))
    finally:
        continue

while len(entries) < numberOfEntries:
    numbers = []

    while len(numbers) < 7:
        number = rand.randrange(1, 36)
        if number not in numbers:
            numbers.append(number)

    numbers.sort()
    numbers.append(rand.randrange(1, 21))

    if numbers not in entries:
        entries.append(numbers)


for entry in entries:
    print(entry)
