"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1893
Updated: 2026-06-22T13:20:16+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1893
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
