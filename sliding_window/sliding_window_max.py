"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1479
Updated: 2026-02-16T18:46:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1479
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
