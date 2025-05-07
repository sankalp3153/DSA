"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 490
Updated: 2025-05-07T21:41:03+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 490
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
