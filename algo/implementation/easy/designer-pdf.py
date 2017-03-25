# https://www.hackerrank.com/challenges/designer-pdf-viewer

import sys

h = list(map(int, input().strip().split(' ')))
word = input().strip()

width = len(word)

heights = list()
for char in word:
    heights.append(h[ord(char.upper()) - 65])

height = max(heights)
print(width * height)
