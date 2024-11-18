#club loyalty
import sys
n = int(input('integer practise'))
club_teams = {}
for line in sys.stdin:
    data = line.split(':')
    teams = data[1].strip().split(',')
    for i in range(len(teams)):
        if teams[i] in club_teams:
            club_teams[teams[i]] += 1
        else:
            club_teams[teams[i]] = 1



for (key,value) in sorted(club_teams.items(),key=lambda x:(-x[1],x[0])):
    if value > n:
        print(key,value)
    else:
        break