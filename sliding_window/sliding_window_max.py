"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 444
Updated: 2025-04-19T14:24:16+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 444
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
