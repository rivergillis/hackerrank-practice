# https://www.hackerrank.com/challenges/strange-advertising

n = int(input().strip())

total_shown = 5
total_liked = 0

for i in range(n):
    liked = int(total_shown / 2)
    #print(liked, "out of", total_shown, "liked it on", i)
    total_liked += liked
    total_shown = liked * 3

print(total_liked)
