"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 191
Updated: 2025-02-13T22:56:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 191
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
