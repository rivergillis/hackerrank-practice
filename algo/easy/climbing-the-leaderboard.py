# https://www.hackerrank.com/challenges/climbing-the-leaderboard

n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]


def build_rankings(l):
    # builds a list of rankings for a list of scores
    rankings = list()

    rankings.append(1)
    prev_score = l[0]
    counter = 1

    for i in range(1, len(l)):
        if l[i] != prev_score:
            counter += 1
        rankings.append(counter)
        prev_score = l[i]

    rankings.append(counter + 1)  # for new worst scores

    return rankings


def reverse_insort_pos(a, x):
    """ find position to insert item x in list a, keep it reverse sorted
    """
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x > a[mid]:
            hi = mid
        else:
            lo = mid + 1

    # makes sure to insert to the left
    if (lo < len(a)):
        while lo > 0 and a[lo - 1] == x:
            lo -= 1
    return lo


rankings = build_rankings(scores)

for alice_score in alice:
    pos = reverse_insort_pos(scores, alice_score)

    if pos == len(scores) and scores[pos - 1] == alice_score:
        # if we're tied for last place, use the ranking before last place
        print(rankings[pos - 1])
    else:
        print(rankings[pos])
