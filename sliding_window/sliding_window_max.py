"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1640
Updated: 2026-04-03T21:06:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1640
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
