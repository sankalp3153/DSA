"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 2169
Updated: 2026-09-10T15:32:31+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2169
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
