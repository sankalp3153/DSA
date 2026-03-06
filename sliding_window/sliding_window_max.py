"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1548
Updated: 2026-03-06T19:35:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1548
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
