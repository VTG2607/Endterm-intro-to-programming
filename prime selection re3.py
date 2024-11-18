import math
import sys

def is_prime(num: int) -> bool:
    d = 2
    if num == 0 or num == 1:
        return False
    else:
        while d <= math.sqrt(num):
            if num % d == 0:
                return False
            d += 1
        return True


def main():
    with open(sys.argv[1]) as file:
        for line in file:
            numbers = []
            data = line.strip('\n').split()

            for num in data:
                if is_prime(int(num)) == 1 and int(num) not in numbers:
                    numbers.append(int(num))
            numbers.sort()
            if numbers:
                print(', '.join(str(p) for p in numbers))
            else:
                print("NOTHING")

if __name__ == '__main__':
    main()



