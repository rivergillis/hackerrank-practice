# https://www.hackerrank.com/challenges/acm-icpc-team

import itertools

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
topic = []
for topic_i in range(n):
    topic_t = str(input().strip())
    topic.append(topic_t)

topic_bin = [int(t, base=2) for t in topic]

best_num = 0
num_groups = 0

for pair in itertools.combinations(topic_bin, r=2):
    x = pair[0]
    y = pair[1]
    num_topics = bin(x | y).count('1')
    if num_topics > best_num:
        best_num = num_topics

for pair in itertools.combinations(topic_bin, r=2):
    x = pair[0]
    y = pair[1]
    num_topics = bin(x | y).count('1')
    if num_topics == best_num:
        num_groups += 1

print(best_num)
print(num_groups)
