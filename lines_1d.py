"""
In lines computer game, a player sets balls of different colors in a line.
When a continuous block of three or more balls of the same color is formed,
it is removed from the line. In this case, all the balls are shifted to each
other, and the situation may be repeated.

Write a function lines(a) that determines how many balls will be destroyed.
There can be at most one continuous block of three or more same-colored
balls at the initial moment.

Input data:
The function takes a list a with initial balls disposition.
Balls number is less or equals 1000, balls colors can be from 0 to 9,
each color has its own integer.

Output data:
The function has to return one number, the number of the balls that will be destroyed.

Input                   Result
1 3 3 3 2               3
3 3 2 1 1 1 2 2 3 3     10
"""


def lines(line):
    balls_count = 0
    i = 0

    while 0 <= i < len(line) - 2:
        current = line[i]
        current_count = 1
        j = i + 1 + balls_count

        while balls_count >= 0 and i > 0:
            if line[i-1] == current:
                current_count += 1
                i -= 1
            else:
                break

        while j < len(line):
            if line[j] == current:
                current_count += 1
                j += 1
            else:
                break

        if current_count >= 3:
            balls_count = j - i

        if balls_count > 0 and current_count < 3:
            break

        if balls_count == 0:
            i = j

        if balls_count > 0:
            i -= 1

    return balls_count


s = list(input().strip().split())
print(lines(s))
