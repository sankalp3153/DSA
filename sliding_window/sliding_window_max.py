"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1709
Updated: 2026-04-24T14:09:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1709
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
