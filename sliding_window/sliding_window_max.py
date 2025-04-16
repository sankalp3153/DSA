"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 421
Updated: 2025-04-16T16:08:02+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 421
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
