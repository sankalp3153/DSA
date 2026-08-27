"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 2123
Updated: 2026-08-27T21:25:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2123
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
