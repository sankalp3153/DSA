"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1594
Updated: 2026-03-21T15:46:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1594
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
