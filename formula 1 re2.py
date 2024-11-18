import sys
formula_1 = {}
with open(sys.argv[1]) as file:
    for line in file:
        data = line.strip('\n').split(';')
        driver_name = data[0]
        laps = int(data[2])
        if driver_name in formula_1:
            formula_1[driver_name] += laps
        else:
            formula_1[driver_name] = laps

print(formula_1)
for (key,value) in sorted(formula_1.items(), key=lambda x:(-x[1], x[0])):
    print(key)