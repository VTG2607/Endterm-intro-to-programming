import sys
from typing import NamedTuple

RollerCoaster = NamedTuple('RollerCoaster',[('coaster_name', str),
                                            ('world_name', str),
                                            ('minimum_height', int),
                                            ('wait_time',int)])

def line_to_coaster(line): #data to tuple
    data = line.strip().split(";")
    return RollerCoaster(data[0], data[1], int(data[2]),int(data[3]))

def coaster_to_line(coaster): # tuple into string data
    return f'{coaster.coaster_name} {coaster.world_name} {coaster.wait_time}'
# parameter 'coaster' should be the one mentioned in return values, else it would not run

def coaster_sort(coasters):
    coasters.sort(key = lambda coaster:(coaster.wait_time,-coaster.minimum_height,coaster.coaster_name))
    return coasters

def main():
    coasters = []
    for line in sys.stdin:
        coasters.append(line_to_coaster(line))
    for coaster in coaster_sort(coasters):
        print(coaster_to_line(coaster))

if __name__ == '__main__':
    main()


#
# import sys
# from typing import NamedTuple
# RollerCoaster = NamedTuple("RollerCoaster", [("name", str), ("world", str),
# ("height", int), ("time", int)])
# def line_to_coaster(line):
#     data = line.strip().split(";")
#     return RollerCoaster(data[0], data[1], int(data[2]), int(data[3]))
# def coaster_to_line(coaster):
#     return f"{coaster.name} ({coaster.world}): {coaster.time}"
# def sort_coasters(coasters):
#     coasters.sort(key = lambda coaster: (coaster.time, -coaster.height, coaster.name))
#     return coasters
# def main():
#     coasters = []
#     for line in sys.stdin:
#         coasters.append(line_to_coaster(line))
#     for coaster in sort_coasters(coasters):
#         print(coaster_to_line(coaster))
#
# if __name__ == '__main__':
#     main()