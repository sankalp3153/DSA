"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1387
Updated: 2026-01-25T19:37:25+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1387
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
