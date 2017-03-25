# https://www.hackerrank.com/challenges/save-the-prisoner

# this is too slow


def save(n, sweets, s):
    sweets -= 1
    while sweets:  # while we have candy
        if s == n:  # if we reach the end, reset
            s = 0
        else:
            s += 1  # increase the id
        sweets -= 1
    return s


t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]

    print(save(n, m, s))
