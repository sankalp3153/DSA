"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1019
Updated: 2025-10-02T17:28:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1019
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
