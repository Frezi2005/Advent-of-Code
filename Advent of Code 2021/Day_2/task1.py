from directions import dirs
hPos = 0
depth = 0

for x in dirs:
    dir = x.split()[0]
    amt = x.split()[1]
    match dir:
        case "forward":
            hPos += int(amt)
        case "down":
            depth += int(amt)
        case "up":
            depth -= int(amt)
print(depth * hPos)