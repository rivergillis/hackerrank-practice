# https://www.hackerrank.com/challenges/kaprekar-numbers

p = int(input().strip())
q = int(input().strip())


def kaprekar(p, q):
    nums = list()
    for i in range(p, q + 1):
        i_str = str(i)
        square_str = str(i**2)
        right_half = square_str[len(square_str) - len(i_str):]
        left_half = square_str[:len(square_str) - len(i_str)]

        if right_half and left_half:
            total_sides = int(right_half) + int(left_half)
        elif left_half:
            total_sides = int(left_half)
        else:
            total_sides = int(right_half)

        if total_sides == i:
            nums.append(i)
    return nums


kaps = kaprekar(p, q)
if kaps:
    for n in kaps:
        print(n, end=' ')
else:
    print("INVALID RANGE")
