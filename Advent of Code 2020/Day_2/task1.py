from passwords import passwords
import re

count = 0

for x in passwords:
    if len(re.findall(x.split(":")[0][-1], x.split(":")[1].strip())) <= int(re.search('\d+-\d+', x.split(":")[0]).group(0).split("-")[1]) and len(re.findall(x.split(":")[0][-1], x.split(":")[1].strip())) >= int(re.search('\d+-\d+', x.split(":")[0]).group(0).split("-")[0]):
        count += 1
print(count)
