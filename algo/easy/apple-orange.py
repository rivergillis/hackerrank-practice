# https://www.hackerrank.com/challenges/apple-and-orange
import sys

s, t = input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = input().strip().split(' ')
m, n = [int(m), int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]


def is_in_bounds(a, s, t):
    # deterimines if s <= a <= t
    return (a >= s and a <= t)

apple_total = 0
orange_total = 0

apple_tree = a
orange_tree = b

for current_apple in apple:
    if is_in_bounds(apple_tree + current_apple, s, t):
        apple_total += 1

for current_orange in orange:
    if is_in_bounds(orange_tree + current_orange, s, t):
        orange_total += 1

print(apple_total)
print(orange_total)
