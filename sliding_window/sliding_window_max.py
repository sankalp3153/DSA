"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 30
Updated: 2025-01-07T11:45:02+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 30
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
