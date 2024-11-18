import sys
from typing import NamedTuple

Minions = NamedTuple("Minions", [('minion_name', str),
                                ('hunger', int),
                                ('motivation', int),
                                ('pants_size', str)])

def line_to_minion(line):
    data = line.strip().split(';')
    return Minions(data[0],int(data[1]),int(data[2]),data[3])

def minion_to_line(minion):
    return f'{minion.minion_name} {minion.hunger} ({minion.pants_size})'

def minions_sort(list):
    list.sort(key = lambda minions:(-minions.motivation, minions.minion_name))
    return list

def main():
    minion_list = []
    for line in sys.stdin:
        minion_list.append(line_to_minion(line))
    for minions in minions_sort(minion_list):
        print(minion_to_line(minions))

if __name__=="__main__":
    main()