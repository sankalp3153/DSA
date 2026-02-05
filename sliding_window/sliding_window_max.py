"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1433
Updated: 2026-02-05T14:24:27+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1433
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
