import math
def count_squares(li: list) -> int:
    count = 0
    for number in li:
        if int(math.sqrt(number))**2 == number:
            count += 1

    return count
print(count_squares([9,4,5,6,7,8,9,10,11]))