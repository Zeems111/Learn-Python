"""
Given an array a, a sliding window of size k is moving
from the very left of the array to the very right.
Each time the sliding window moves right by one position.
For each sliding window position return minimum value
of all numbers inside the sliding window.

"""


def sliding_window_min(a, k):
    q = []
    for i in range(len(a)):
        if q:
            if q[0] < i - k + 1:
                del q[0]
            while q and a[i] <= a[q[-1]]:
                q.pop()
        q.append(i)
        if i >= k-1:
            print("min:", a[q[0]], "\twindow:", a[i-k+1:i+1])

if __name__ == '__main__':
    k = int(input())

    arr = list(map(int, input().split()))
    sliding_window_min(arr, k)
