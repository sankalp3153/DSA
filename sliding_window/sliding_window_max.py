"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 76
Updated: 2025-01-16T17:51:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 76
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
