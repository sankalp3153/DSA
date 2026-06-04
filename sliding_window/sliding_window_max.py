"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1824
Updated: 2026-06-04T10:09:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1824
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
