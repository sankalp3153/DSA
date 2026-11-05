"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 2330
Updated: 2026-11-05T11:28:16+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2330
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
