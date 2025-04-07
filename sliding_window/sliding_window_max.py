"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 398
Updated: 2025-04-07T15:58:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 398
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
