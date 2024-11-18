import sys
from typing import NamedTuple


RollerCoaster = NamedTuple('RollerCoaster',[('coaster_name', str),
                                            ('world_name', str),
                                            ('minimum_height', int),
                                            ('wait_time', int)])
def line_to_coaster(line):
    data = line.strip().split(';')
    return RollerCoaster(data[0],data[1],int(data[2]),int(data[3]))   #creating new data type

def coaster_to_line(coaster):
    return f'{coaster.coaster_name} {coaster.world_name}:{coaster.wait_time}'

def sort_coasters(coasters):
        coasters.sort(key=lambda coasters:(coasters.wait_time, -coasters.minimum_height,coasters.coaster_name))
        return coasters

def main():
    roller_list = []
    for line in sys.stdin:
        roller_list.append(line_to_coaster(line))
    for RollerCoasters in sort_coasters(roller_list):
        print(coaster_to_line(RollerCoasters))

if __name__ == "__main__":
    main()
