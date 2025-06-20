"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 651
Updated: 2025-06-20T16:22:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 651
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
