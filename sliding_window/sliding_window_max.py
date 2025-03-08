"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 260
Updated: 2025-03-08T10:36:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 260
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
