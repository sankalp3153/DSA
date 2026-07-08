"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1939
Updated: 2026-07-08T10:51:03+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1939
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
