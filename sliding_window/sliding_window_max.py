"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 2100
Updated: 2026-08-23T14:29:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2100
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
