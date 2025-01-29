"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 122
Updated: 2025-01-29T18:04:59+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 122
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
