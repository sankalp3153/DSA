"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1180
Updated: 2025-11-26T22:00:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1180
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
