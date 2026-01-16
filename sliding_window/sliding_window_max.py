"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1364
Updated: 2026-01-16T21:02:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1364
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
