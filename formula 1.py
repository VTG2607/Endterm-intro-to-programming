import sys
drivers = {}

with open(sys.argv[1]) as file:
        for line in file:
            line = line.strip('\n')
            data = line.split(';')
            name = data[0]
            if name in drivers:
                drivers[name] += int(data[2])
            else:
                drivers[name] = int(data[2])

for (key, value) in sorted(drivers.items(), key=lambda x:(-x[1], x[0])):
    print('Key: {}'.format(key))