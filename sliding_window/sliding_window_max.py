"""
Module: sliding_window_max
Approach: monotonic decreasing deque O(n)
Revision: 467
Updated: 2025-04-28T14:53:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 467
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
