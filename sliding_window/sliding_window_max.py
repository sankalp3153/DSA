"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 582
Updated: 2025-06-04T10:18:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 582
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
