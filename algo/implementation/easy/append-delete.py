# https://www.hackerrank.com/challenges/append-and-delete

# works but is too slow!
import sys

s = input().strip()
t = input().strip()
k = int(input().strip())


def permute(s, t, k):
    common_len = 0
    min_len = min([len(s), len(t)])
    max_len = max([len(s), len(t)])

    for i in range(min_len):
        if [s] == t[i]:
            common_len += 1
        else:
            break

    # case A
    # we need to have enough moves to even the lengths
    if (len(s) + len(t) - 2 * common_len) > k:
        # if k < (max_len - common_len):
        return False
    # case B
    # odd len mismtaches need odd moves
    elif (len(s) + len(t) - 2 * common_len) % 2 == k % 2:
        # elif (max_len - common_len) % 2 == k % 2:
        return True
    # case C
    # we can completely delete and rebuild
    elif (len(s) + len(t) - k) < 0:
        return True
    # other cases will fail
    else:
        return False

if permute(s, t, k):
    print("Yes")
else:
    print("No")
