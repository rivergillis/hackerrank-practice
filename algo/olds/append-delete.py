# https://www.hackerrank.com/challenges/append-and-delete

# works but is too slow!
import sys

s = input().strip()
t = input().strip()
k = int(input().strip())


def append(s, t):
    # appends a char from t onto s depending on how long s is
    # constaint: len(s) < len(t)
    return s + t[len(s)]


def delete(s):
    # deletes the last char from s, empty returns empty
    if s:
        return s[:-1]
    else:
        return ""


def permute(s, t, k):
    print("permute with s=", s, "t=", t, "k=", k)
    if s == t:   # matched the strings
        if k % 2 == 0:  # did it with the right number
            return True
    if k < 0:  # exhausted all possibles
        return False

    # recursive cases
    if len(s) < len(t):  # can still append
        return permute(append(s, t), t, k - 1) or permute(delete(s), t, k - 1)
    else:  # can no longer append
        return permute(delete(s), t, k - 1)

    print("Yes")
else:
    print("No")
