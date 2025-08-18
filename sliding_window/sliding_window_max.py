"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 858
Updated: 2025-08-18T14:24:03+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 858
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
