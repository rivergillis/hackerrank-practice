# https://www.hackerrank.com/challenges/equality-in-a-array

n = int(input().strip())
a = [int(x) for x in input().strip().split(' ')]

most_common_len = a.count(max(set(a), key=a.count))
print(len(a) - most_common_len)
