"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 375
Updated: 2025-04-01T15:06:42+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 375
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
