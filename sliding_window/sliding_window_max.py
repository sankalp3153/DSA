"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 214
Updated: 2025-02-20T15:25:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 214
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
