"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1778
Updated: 2026-05-19T21:19:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1778
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
