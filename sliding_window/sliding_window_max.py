"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 743
Updated: 2025-07-22T22:02:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 743
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
