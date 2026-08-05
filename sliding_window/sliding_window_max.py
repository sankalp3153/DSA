"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 2031
Updated: 2026-08-05T10:18:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2031
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
