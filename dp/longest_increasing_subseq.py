"""
Longest Increasing Subsequence via Patience Sorting & Binary Search.
Time: O(n log n) | Space: O(n)
"""

from bisect import bisect_left
from typing import List


def length_of_lis(nums: List[int]) -> int:
    tails: List[int] = []
    for num in nums:
        pos = bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)
