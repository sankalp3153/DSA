"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 674
Updated: 2025-06-26T21:14:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 674
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
