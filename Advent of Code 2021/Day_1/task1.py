from readings import readings
previousReading = readings[0];
count = 0

for x in readings:
    if x > previousReading:
        count += 1
    previousReading = x
print(count)