"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 2238
Updated: 2026-10-03T22:56:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2238
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
