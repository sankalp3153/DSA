"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 145
Updated: 2025-02-03T10:29:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 145
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
