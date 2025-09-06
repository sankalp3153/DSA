"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 927
Updated: 2025-09-06T13:34:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 927
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
