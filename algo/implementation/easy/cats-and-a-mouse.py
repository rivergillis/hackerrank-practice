# https://www.hackerrank.com/challenges/cats-and-a-mouse


def distance(x1, x2):
    return abs(x1 - x2)

q = int(input().strip())
for a0 in range(q):
    x, y, z = input().strip().split(' ')
    x, y, z = [int(x), int(y), int(z)]

    if distance(x, z) == distance(y, z):
        print("Mouse C")
    elif distance(x, z) > distance(y, z):
        print("Cat B")
    else:
        print("Cat A")
