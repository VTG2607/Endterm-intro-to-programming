import sys
festival_bands = {}
for line in sys.stdin:
    data = line.split(':')
    bands = data[1].strip().split(',') # stripping needed for intact strings
    for i in range(len(bands)):
        if bands[i] in festival_bands:
            festival_bands[bands[i]] += 1
        else:
            festival_bands[bands[i]] = 1
for (key,values) in sorted(festival_bands.items()):
    print(key,values)