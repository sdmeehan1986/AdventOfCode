elves = []
for house in range(750000, 33100000):
    tmp = 0
    for elf in range(0, house):
        if (house % (elf+1)) == 0:
            tmp += (elf+1) * 10
    print(f'House number {house}, has {tmp} number of presents')
    if tmp >= 33100000:
        break

