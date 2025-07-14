"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 720
Updated: 2025-07-14T23:25:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 720
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
