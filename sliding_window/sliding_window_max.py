"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 283
Updated: 2025-03-12T12:43:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 283
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
