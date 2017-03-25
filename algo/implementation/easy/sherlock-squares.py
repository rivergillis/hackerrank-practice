# https://www.hackerrank.com/challenges/sherlock-and-squares
import math

# count the integers between the square roots
# of starting and ending nums

t = int(input().strip())

for a0 in range(t):
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]

    print(int(math.floor(sqrt(b)) - math.ceil(math.sqrt(a)) + 1))
