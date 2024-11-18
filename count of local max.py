import sys


def countOfLocalMax(l: list) -> int:
    count = 0

    for i in range(1, len(l) - 1):
        num = l[i]
        if (num > l[i-1]) and (num > l[i+1]):
            count += 1

    return count

def main():
    list = sys.argv[1:]
    for i in range(len(list)):
        list[i] = int(list[i])

    print(countOfLocalMax(list))

if __name__ == "_main_":
    main()



















