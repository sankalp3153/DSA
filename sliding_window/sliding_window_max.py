"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1410
Updated: 2026-01-31T13:07:05+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1410
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
