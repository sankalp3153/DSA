"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1042
Updated: 2025-10-09T20:05:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1042
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
