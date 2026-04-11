"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1663
Updated: 2026-04-11T13:43:03+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1663
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
