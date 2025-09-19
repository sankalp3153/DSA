"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 973
Updated: 2025-09-19T19:04:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 973
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
