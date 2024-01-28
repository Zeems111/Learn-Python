"""
A landscape in a Flat World consists of blocks size 1 by 1 meter.
The island is a set of different height columns consist of
stone and surrounded by the sea.
Heavy rain have fallen over the island, and filled all the lowlands
with water. Extra water has gone back into the sea, without
increasing its level. According to the landscape of the island,
determine how many blocks of water remain after rain in the lowlands
on the island.

Implement a function calc_rain_water(h) which takes the landscape of
the island and returns the number of remaining water blocks.

Input:
11
2 5 2 3 6 9 1 3 4 6 1
Output: 15

Input:
11
2 5 2 3 6 6 1 3 4 6 1
Output: 15

Input:
11
5 5 2 3 6 6 1 3 4 6 1
Output: 15

Input:
11
2 5 2 3 6 9 1 3 4 6 6
Output: 15

Input:
11
2 5 2 3 6 9 1 3 4 6 7
Output: 19

Input:
11
2 5 2 3 9 6 1 3 4 6 2
"""


def calc_rain_water(h):
    boundary = []
    total_water = 0

    for i in range(len(h)):
        while len(boundary) != 0 and (h[boundary[-1]] < h[i]):
            last_h = h[boundary[-1]]
            boundary.pop()

            if len(boundary) == 0:
                break

            width = i - boundary[-1] - 1
            min_height = min(h[boundary[-1]], h[i]) - last_h
            total_water += width * min_height

        boundary.append(i)

    return total_water


n = int(input())
landscape = list(map(int, input().split()))
print(calc_rain_water(landscape))
