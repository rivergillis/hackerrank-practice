# https://www.hackerrank.com/challenges/library-fine

import datetime


def calc_fine(initial, final):
    delta = final - initial

    if delta.days <= 0:
        return 0
    if final.month == initial.month and final.year == initial.year:
        return 15 * delta.days
    elif final.year == initial.year:
        return 500 * (final.month - initial.month)
    else:
        return 10000


d1, m1, y1 = input().strip().split(' ')
d1, m1, y1 = [int(d1), int(m1), int(y1)]
d2, m2, y2 = input().strip().split(' ')
d2, m2, y2 = [int(d2), int(m2), int(y2)]

final = datetime.date(y1, m1, d1)
initial = datetime.date(y2, m2, d2)

print(calc_fine(initial, final))
