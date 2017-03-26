# https://www.hackerrank.com/challenges/chocolate-feast


def find_amount(dollars, price, wrapper_price):
    chocolates = dollars // price
    wrappers = 0
    total_bought = 0
    while chocolates:
        total_bought += chocolates
        wrappers += chocolates
        can_buy = wrappers // wrapper_price
        wrappers = wrappers % wrapper_price
        chocolates = can_buy

    return total_bought

t = int(input().strip())
for a0 in range(t):
    n, c, m = input().strip().split(' ')
    n, c, m = [int(n), int(c), int(m)]

    print(find_amount(n, c, m))
