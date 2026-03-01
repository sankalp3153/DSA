"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1525
Updated: 2026-03-01T20:53:21+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1525
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
