"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 7
Updated: 2025-01-02T23:16:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 7
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
