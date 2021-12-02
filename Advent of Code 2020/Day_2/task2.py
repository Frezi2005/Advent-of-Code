from passwords import passwords
import re

count = 0

for x in passwords:
    firstIndex = int(re.search('\d+-\d+', x.split(":")[0]).group(0).split("-")[0])
    secondIndex = int(re.search('\d+-\d+', x.split(":")[0]).group(0).split("-")[1])
    if (x.split(":")[1].strip()[firstIndex - 1] == x.split(":")[0][-1] and x.split(":")[1].strip()[secondIndex - 1] != x.split(":")[0][-1]) or (x.split(":")[1].strip()[firstIndex - 1] != x.split(":")[0][-1] and x.split(":")[1].strip()[secondIndex - 1] == x.split(":")[0][-1]):
        count += 1
print(count)
