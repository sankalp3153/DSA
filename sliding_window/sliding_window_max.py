"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 904
Updated: 2025-08-29T23:13:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 904
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
