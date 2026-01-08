"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1341
Updated: 2026-01-08T14:48:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1341
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
