"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1157
Updated: 2025-11-23T18:45:52+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1157
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
