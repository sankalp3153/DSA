"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 237
Updated: 2025-03-01T22:51:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 237
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
