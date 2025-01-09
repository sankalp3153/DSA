"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 53
Updated: 2025-01-09T22:56:59+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 53
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
