from readings import readings
previousReading = readings[0] + readings[1] + readings[2]
count = 0

for x in range(0, len(readings)):
    if x < len(readings) and x + 1 < len(readings) and x + 2 < len(readings):
        if readings[x] + readings[x + 1] + readings[x + 2] > previousReading:
            count += 1
        previousReading = readings[x] + readings[x + 1] + readings[x + 2]
print(count)