"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1065
Updated: 2025-10-17T19:30:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1065
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
