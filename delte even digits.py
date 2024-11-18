import sys

def del_even(line) -> str:
    return ''.join(c for c in line if c not in '02468')





def main():
    n = input('data:')
    while n != '':
        print(del_even(n))
        n = input()

if __name__ == '__main__':
    main()