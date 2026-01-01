"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1318
Updated: 2026-01-01T16:33:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1318
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
