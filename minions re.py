import sys
from typing import NamedTuple

Minions = NamedTuple('Minions', [('minion_name', str),
                                ('hunger', int),
                                ('motivation', int),
                                ('pants_size', str)])

def line_to_minion(line):
    data = line.strip().split(';')
    return Minions(data[0],int(data[1]),int(data[2]),data[3])

def minion_to_line(minions):
    return f'{minions.minion_name} {minions.hunger} {minions.pants_size}'

def sort_minions(minion_items):
    minion_items.sort(key=lambda minion_items: (-minion_items.motivation, minion_items.minion_name))
    return minion_items

def main():
    with open('minions.txt') as file:
        minions = []
        for line in sys.stdin:
            minions.append(line_to_minion(line))
        for minion_parameters in sort_minions(minions):
            print(minion_to_line(minion_parameters))

if __name__ == "__main__":
    main()

# import sys
# from typing import NamedTuple
# Minion = NamedTuple("Minion", [("name", str), ("hunger", int), ("motivation", int),
# ("size", str)])
# def minion_to_line(minion):
#     return f"{minion.name} {minion.hunger} ({minion.size})"
# def line_to_minion(line):
#     data = line.strip().split(";")
#     return Minion(data[0], int(data[1]), int(data[2]), data[3])
# def sort_minions(minions):
#     minions.sort(key=lambda minions: (-minions.motivation, minions.name))
#     return minions
# def main():
#     minions = []
#     for line in sys.stdin:
#         minions.append(line_to_minion(line))
#     for minion in sort_minions(minions):
#         print(minion_to_line(minion))
# if __name__ == '__main__':
#     main()