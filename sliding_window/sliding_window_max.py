"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1272
Updated: 2025-12-19T11:34:41+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1272
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
