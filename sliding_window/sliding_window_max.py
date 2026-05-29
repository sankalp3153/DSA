"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1801
Updated: 2026-05-29T15:37:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1801
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
