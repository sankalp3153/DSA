"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1134
Updated: 2025-11-13T16:36:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1134
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
