# https://www.hackerrank.com/challenges/save-the-prisoner

# this is too slow


def save(n, sweets, s):
    sweets -= 1
    s += sweets
    while s > n:
        s -= n
    return s


t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]

    print(save(n, m, s))
