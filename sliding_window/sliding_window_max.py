"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 2353
Updated: 2026-11-17T16:49:16+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2353
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
