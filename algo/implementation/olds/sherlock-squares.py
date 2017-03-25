# https://www.hackerrank.com/challenges/sherlock-and-squares
import math

# this works but is too slow. count the integers between the square roots
# of starting and ending nums

t = int(input().strip())
is_squares = dict()


def digital_root(s):
    total = 0
    for digit in s:
        total += int(digit)

    while total > 9:
        new_total = 0
        for digit in str(total):
            new_total += int(digit)
        total = new_total
    return total


def is_square(num):
    s = str(num)
    # print(s)

    if s.endswith(('2', '3', '7', '8')):
        #print("false on ending wrong")
        return False

    if len(s) > 1:
        if s.endswith('6'):
            if int(s[-2]) % 2 == 0:
                #print("false on ending with 6 with even tens")
                return False
        else:
            if int(s[-2]) % 2 == 1:
                #print("false on ending not 6 with odd tens")
                return False
        if s.endswith('5'):
            if s[-2] != '2':
                #print("false on ending 5 with nontwo tens")
                return False

        if int(s[-1]) % 2 == 0:
            if int(s[-2:]) % 4 != 0:
                #print("false on even with nondivisble by 4 last two")
                return False

    dig_root = str(digital_root(s))
    #print("dig root is", dig_root)
    if dig_root.endswith(('2', '3', '5', '6', '8', '0')):
        return False

    root = math.sqrt(num)
    return root == int(root)


for a0 in range(t):
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]

    total = 0

    for i in range(a, b + 1):
        result = is_squares.get(i, is_square(i))
        #print(i, result)
        if result:
            total += 1
        is_squares[i] = result

    print(total)
