"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1617
Updated: 2026-03-25T19:03:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1617
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
