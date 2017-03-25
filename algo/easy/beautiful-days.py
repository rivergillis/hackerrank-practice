# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies

import math


def get_length(n):
    # returns the length of integer n:
    if (n == 0):
        return 1

    length = 0
    divisor = 1

    while int(n / divisor) >= 1:
        length += 1
        divisor *= 10

    return length


def reverse_num(n):
    # returns an integer of the reversed number
    # 21 returns 12, 10 returns 1
    length = get_length(n)

    reversed = 0
    divisor = 10

    while length > 0:
        bottom = math.floor(n % divisor)
        current_digit = math.floor(bottom / (divisor / 10))
        addition = (current_digit * (10**length)) / 10

        reversed += int(addition)

        divisor *= 10
        length -= 1

    return reversed

i, j, k = input().strip().split(' ')
i, j, k = [int(i), int(j), int(k)]

total_days = 0

for day in range(i, j + 1):
    # using all that shit above is actually slower, just convert it a bunch
    # and let python optimize
    result = abs(day - (int(str(day)[::-1]))) / k

    if (result == int(result)):  # is a whole num
        total_days += 1

print(total_days)
