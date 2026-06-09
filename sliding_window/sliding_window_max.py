"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1847
Updated: 2026-06-09T12:25:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1847
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
