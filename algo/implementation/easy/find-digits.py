# https://www.hackerrank.com/challenges/find-digits


def count_divisibles(n, n_str):
    # returns the number of times each digit of n_str divides n
    divisibles = 0
    for n_char in n_str:
        digit = int(n_char)
        if digit == 0:
            continue
        elif n % digit == 0:
            divisibles += 1
    return divisibles


t = int(input().strip())
for a0 in range(t):
    n_str = input().strip()
    n = int(n_str)
    print(count_divisibles(n, n_str))
