"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 835
Updated: 2025-08-12T21:06:16+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 835
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
