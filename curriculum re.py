# import sys
#
# db = {}
# n = int(input("N? "))
#
# for line in sys.stdin:
#     data = line.strip().split(':')
#     code = data[0].split('-')
#     rec_sem = int(code[1])
#     unique_id = int(code[2])
#     subject = data[1]
#
#     db[subject] = [rec_sem,unique_id]
# for (key,value) in sorted(db.items(),key =lambda x:(x[1][0], x[1][1])):
#     print(key)
#
import sys

db = {}
n = int(input("N? "))

for line in sys.stdin:
    line = line.strip().split(':')
    code = line[0]
    name = line[1]
    cNumber = line[2]

    recSemester = int(code.split('-')[1])
    unique = int(code.split('-')[2])
    db[name] = [recSemester, unique]

print(db)
for key, value in sorted(db.items(), key=lambda x: (x[1][0], x[1][1])):
    print(key)