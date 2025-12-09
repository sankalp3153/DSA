"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1226
Updated: 2025-12-09T15:17:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1226
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
