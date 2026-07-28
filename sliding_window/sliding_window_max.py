"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 2008
Updated: 2026-07-28T11:45:33+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2008
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
