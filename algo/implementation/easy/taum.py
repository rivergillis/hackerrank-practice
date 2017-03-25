# https://www.hackerrank.com/challenges/taum-and-bday


def find_cost(num_blacks, num_whites, black_cost, white_cost, conversion_cost):
    white_cheapest = min([white_cost, black_cost + conversion_cost])
    black_cheapest = min([black_cost, white_cost + conversion_cost])

    return (black_cheapest * num_blacks) + (white_cheapest * num_whites)

t = int(input().strip())
for a0 in range(t):
    b, w = input().strip().split(' ')
    b, w = [int(b), int(w)]
    x, y, z = input().strip().split(' ')
    x, y, z = [int(x), int(y), int(z)]

    print(find_cost(b, w, x, y, z))
