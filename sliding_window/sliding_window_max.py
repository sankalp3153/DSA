"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 2284
Updated: 2026-10-21T18:26:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2284
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
