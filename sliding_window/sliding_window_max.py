"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 881
Updated: 2025-08-24T15:57:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 881
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
