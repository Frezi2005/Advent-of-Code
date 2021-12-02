from report import numbers

for i in numbers:
    for j in numbers:
        for k in numbers:
            if i + j + k == 2020:
                print(i * j * k)