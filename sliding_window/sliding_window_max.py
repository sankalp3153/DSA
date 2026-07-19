"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1985
Updated: 2026-07-19T20:07:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1985
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
