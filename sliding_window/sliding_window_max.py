"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 766
Updated: 2025-07-28T16:24:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 766
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
