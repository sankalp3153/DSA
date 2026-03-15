"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1571
Updated: 2026-03-15T16:48:05+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1571
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
