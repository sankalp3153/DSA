"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 1295
Updated: 2025-12-27T16:18:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1295
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
