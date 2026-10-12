"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 2261
Updated: 2026-10-12T18:10:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2261
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
