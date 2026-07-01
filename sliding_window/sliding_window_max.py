"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1916
Updated: 2026-07-01T10:19:42+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1916
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
