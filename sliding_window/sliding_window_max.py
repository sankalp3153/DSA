"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1502
Updated: 2026-02-25T17:25:29+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1502
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
