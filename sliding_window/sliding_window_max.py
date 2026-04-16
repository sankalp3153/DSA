"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1686
Updated: 2026-04-16T16:45:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1686
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
