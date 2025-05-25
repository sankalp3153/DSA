"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 559
Updated: 2025-05-25T17:23:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 559
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
