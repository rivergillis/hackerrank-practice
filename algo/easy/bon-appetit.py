# https://www.hackerrank.com/challenges/bon-appetit

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
c = [int(a_temp) for a_temp in input().strip().split(' ')]
b = int(input().strip())

total_owed = sum(c)
total_owed -= c[k]
total_owed /= 2

if (b == total_owed):
    print("Bon Appetit")
else:
    print(int(b - total_owed))
