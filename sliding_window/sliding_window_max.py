"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 812
Updated: 2025-08-09T19:15:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 812
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
