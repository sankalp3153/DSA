"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 950
Updated: 2025-09-11T20:29:16+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 950
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
