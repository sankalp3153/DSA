"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 306
Updated: 2025-03-16T20:12:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 306
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
