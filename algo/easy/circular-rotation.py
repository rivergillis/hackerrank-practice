# https://www.hackerrank.com/challenges/circular-array-rotation


def rotate_right(l, n):
    # rotates list l right by n increments
    while n > len(l):
        n -= len(l)

    new_list = list()
    for i in range(len(l)):
        if i < n:
            new_list.append(l[-1 + i - (n - 1)])
        else:
            new_list.append(l[i - n])

    return new_list

l = [1, 2, 3, 4, 5, 6, 7]
rotate_right(l, len(l) + 1)

n, k, q = input().strip().split(' ')
n, k, q = [int(n), int(k), int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
rotated = rotate_right(a, k)

for a0 in range(q):
    m = int(input().strip())
    print(rotated[m])
