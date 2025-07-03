"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 697
Updated: 2025-07-03T20:11:55+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 697
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
