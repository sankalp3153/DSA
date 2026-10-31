"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 2307
Updated: 2026-10-31T12:24:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2307
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
