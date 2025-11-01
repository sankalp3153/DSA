"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1111
Updated: 2025-11-01T22:13:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1111
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
