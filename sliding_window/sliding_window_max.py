"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 536
Updated: 2025-05-22T14:07:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 536
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
