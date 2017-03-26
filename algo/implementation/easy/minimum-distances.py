# https://www.hackerrank.com/challenges/minimum-distances


n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]

minimum = -1

A_set = set(A)

for current_num in A_set:
    begin_spot = None
    end_spot = None

    for i in range(len(A)):
        if A[i] == current_num:
            if begin_spot != None:
                end_spot = i
                if end_spot - begin_spot < minimum or minimum < 0:
                    minimum = end_spot - begin_spot
                    begin_spot = None
                    end_spot = None
            else:
                begin_spot = i

print(minimum)
