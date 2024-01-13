"""
Given a string s. Write a function largest_palindrome(s)
that finds palindrome substring in s with the maximum possible length
"""


# your code
def largest_palindrome(s):
    center = 0
    odd_even = 0
    start = 0
    end = 0

    while center < len(s):
        i = 0
        while center - i >= 0 and center + odd_even + i < len(s):
            if s[center-i] != s[center+odd_even+i]:
                i -= 1
                break

            pal_len = 2 * i + 1 + odd_even
            if pal_len > end - start + 1:
                start = center - i
                end = center + odd_even + i
            i += 1

        if center + 1 < len(s) and s[center] == s[center+1]:
            odd_even = 1 - odd_even
        center += 1 - odd_even

    return s[start: end + 1]


s = input()
print(largest_palindrome(s))