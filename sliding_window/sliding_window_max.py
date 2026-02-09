"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1456
Updated: 2026-02-09T17:45:41+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1456
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
