from directions import dirs
hPos = 0
depth = 0
aim = 0

for x in dirs:
    dir = x.split()[0]
    amt = x.split()[1]
    match dir:
        case "forward":
            hPos += int(amt)
            depth += aim * int(amt)
        case "down":
            aim += int(amt)
        case "up":
            aim -= int(amt)

print(hPos * depth)