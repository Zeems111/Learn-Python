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


def crw(h):
    total_water = 0
    land = 0
    pos = []

    for i in range(len(h)):
        print("Beginning:", pos, sep=' ')
        if not pos:
            pos.append(i)
        elif h[pos[-1]] > h[i]:
            land += h[i]
            print("land", land)
        elif h[pos[-1]] <= h[i]:
            height = min(h[pos[-1]], h[i])
            width = i - pos.pop() - 1
            total_water += height * width - land
            land = 0
            pos.append(i)
        print("End:", pos, sep=' ')
        print("land", land)
        print("water", total_water)

    if pos and pos[-1] < len(h) - 1:
        last = -2 if h[-2] > h[-1] else -1
        height = min(h[pos[-1]], h[last])
        width = len(h) - 1 - pos.pop() - 1
        land -= h[-1]

        total_water += height * width - land
        total_water = 0 if total_water < 0 else total_water
    return total_water


n = int(input())
landscape = list(map(int, input().split()))
#print(calc_rain_water(landscape))
print(crw(landscape))
