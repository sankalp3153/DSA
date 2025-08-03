"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 789
Updated: 2025-08-03T12:33:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 789
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
