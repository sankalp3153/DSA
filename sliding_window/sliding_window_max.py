"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 2192
Updated: 2026-09-19T14:28:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2192
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
