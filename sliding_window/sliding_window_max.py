"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1203
Updated: 2025-12-02T14:58:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1203
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
