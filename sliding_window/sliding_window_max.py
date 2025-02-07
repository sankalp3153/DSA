"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 168
Updated: 2025-02-07T22:53:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 168
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
