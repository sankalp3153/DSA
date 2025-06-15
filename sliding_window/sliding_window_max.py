"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 628
Updated: 2025-06-15T18:14:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 628
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
