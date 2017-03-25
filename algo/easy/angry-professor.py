# https://www.hackerrank.com/challenges/angry-professor

t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]

    present = [x for x in a if x <= 0]

    if len(present) >= k:
        print("NO")
    else:
        print("YES")
