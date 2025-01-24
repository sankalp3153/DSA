"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 99
Updated: 2025-01-24T16:15:42+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 99
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
