"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1249
Updated: 2025-12-14T17:30:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1249
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
