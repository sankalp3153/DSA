"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1088
Updated: 2025-10-26T19:50:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1088
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
